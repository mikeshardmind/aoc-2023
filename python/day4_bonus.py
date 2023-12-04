# an improvement on my original solution that avoids an issue of
# ever holding too gigantic a list in memory
from collections.abc import Iterable
from pathlib import Path
from queue import SimpleQueue

path = Path(__file__).parent.with_name("inputs") / "day4.txt"


def solver() -> tuple[int, int]:
    with path.open(mode="r", encoding="utf-8") as fp:
        scratchcard = fp.read().splitlines()

    card_games: dict[int, int] = {}
    for gamenum, line in enumerate(scratchcard, 1):
        _game_header, game_data = line.split(":")
        winners, ours = ({n for n in x.split(" ") if n} for x in game_data.split("|"))
        card_games[gamenum] = len(winners & ours)

    points = sum(1 << our_wins - 1 for our_wins in card_games.values() if our_wins)

    all_cards_queue: SimpleQueue[Iterable[int]] = SimpleQueue()
    all_cards_queue.put(card_games.keys())
    card_count = 0
    while not all_cards_queue.empty():
        card_iter = all_cards_queue.get()
        for card in card_iter:
            card_count += 1
            all_cards_queue.put(range(1 + card, 1 + card + card_games.get(card, 0)))
    return points, card_count


if __name__ == "__main__":
    print(solver())
