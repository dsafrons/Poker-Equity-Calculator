class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.num_value = int(value) if value.isnumeric() else {"Ace": 14, "King": 13, "Queen": 12, "Jack": 11}[value]

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Hand:
    def __init__(self, c1=None, c2=None):
        self.cards = []
        if c1: self.cards.append(c1)
        if c2: self.cards.append(c2)

    def __repr__(self):
        if not self.cards:
            return "Empty Hand"

        ret = f"{self.cards[0]}"
        if len(self.cards) == 2: ret += f" & {self.cards[1]}"

        return ret

    def add(self, c1, c2=None):
        if len(self.cards) == 2:
            raise Exception("Hand is full")
        if len(self.cards) == 1 and c2:
            raise Exception("1 Card in Hand: Adding Too Many Cards")

        self.cards.append(c1)
        if c2: self.cards.append(c2)
