from dataclasses import dataclass, field


@dataclass(slots=True)
class Card:
    value: str = field(init=True)
    suit: str = field(init=True)
    num_value: int = field(init=False)

    def __post_init__(self):
        value_conversion = {"T": "10", "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
        if len(self.value) == 1:
            if self.value in value_conversion.keys():
                self.value = value_conversion[self.value]

        suit_conversion = {"H": "Hearts", "C": "Clubs", "D": "Diamonds", "S": "Spades"}
        if len(self.suit) == 1:
            self.suit = suit_conversion[self.suit]

        self.num_value = int(self.value) if self.value.isnumeric() else \
            {"Ace": 14, "King": 13, "Queen": 12, "Jack": 11}[self.value]

    @property
    def shorten_value(self):
        shorten_map = {"Ace": "A", "King": "K", "Queen": "Q", "Jack": "J"}
        if self.value in shorten_map.keys():
            return shorten_map[self.value]

        return self.value


    def __eq__(self, other):
        return isinstance(other, Card) and self.value == other.value and self.suit == other.suit

    def __hash__(self):
        return hash((self.value, self.suit))

    def __repr__(self):
        symbol_map = {'Clubs': '♣', 'Diamonds': '♦', 'Hearts': '♥', 'Spades': '♠'}
        return f"{self.shorten_value}{symbol_map[self.suit]}"


class Hole:
    def __init__(self, c1=None, c2=None):
        self.cards = []
        if c1: self.cards.append(c1)
        if c2: self.cards.append(c2)

    def __repr__(self):
        if not self.cards:
            return "No hole cards"

        ret = f"{self.cards[0]}"
        if len(self.cards) == 2: ret += f" & {self.cards[1]}"

        return ret

    def add(self, c1, c2=None):
        if len(self.cards) == 2:
            raise Exception("Hole is full")
        if len(self.cards) == 1 and c2:
            raise Exception("1 Card in Hole: Adding Too Many Cards")

        self.cards.append(c1)
        if c2: self.cards.append(c2)


class CardHelper:
    @staticmethod
    def num_value(value):
        return int(value) if value.isnumeric() else {"Ace": 14, "King": 13, "Queen": 12, "Jack": 11, "Ace2": 1}[value]
