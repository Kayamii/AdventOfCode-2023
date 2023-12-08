letter_map = {"T": "A", "J": "?", "Q": "C", "K": "D", "A": "E"}


def score(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def change(hand):
    if hand == "":
        return [""]

    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in change(hand[1:])
    ]


def rank(hand):
    return max(map(score, change(hand)))


def strn(hand):
    return (rank(hand), [letter_map.get(card, card) for card in hand])


plays = []

file_path="Day7/example.txt"
for line in open(file_path, "r"):
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key=lambda play: strn(play[0]))

total = 0

for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

print(total)