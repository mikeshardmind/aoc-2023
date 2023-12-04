# an improvement on my original solution that avoids an issue of
# ever holding too gigantic a list in memory
from pathlib import Path

path = Path(__file__).parent.with_name("inputs") / "day4.txt"

def solver() -> tuple[int, int]:
    with path.open(mode="r", encoding="utf-8") as fp:
        scratchcard = fp.read().splitlines()

    card_games: list[int] = []
    for line in scratchcard:
        _game_header, game_data = line.split(":")
        winners, ours = ({n for n in x.split(" ") if n} for x in game_data.split("|"))
        card_games.append(len(winners & ours))

    points = sum(1 << our_wins - 1 for our_wins in card_games if our_wins)

    idx = len(card_games) - 1
    while idx > -1:
        current = card_games[idx]
        card_games[idx] = sum(card_games[idx + 1: idx + 1 + current]) + 1
        idx -= 1

    return points, sum(card_games)

if __name__ == "__main__":
    print(solver())
