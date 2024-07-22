from random import choices


class Game:
    def __init__(self, num_players):
        self.deck = [Card(v, s) for s in ["Hearts", "Clubs", "Diamonds", "Spades"]
                     for v in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]
        self.hands = [Hand() for _ in range(num_players)]
        self.deal()

    def deal(self):
        for hand in self.hands:
            cards = choices(self.deck, k=2)
            hand.add(cards[0], cards[1])
            self.deck = [c for c in self.deck if c not in cards]


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

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


if __name__ == "__main__":
    game = Game(4)
