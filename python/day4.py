from pathlib import Path

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

    all_cards = list(card_games.keys())
    for card in all_cards:
        all_cards.extend(range(card + 1, card + 1 + card_games.get(card, 0)))

    return points, len(all_cards)


if __name__ == "__main__":
    print(solver())
