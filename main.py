class Game:
    def __init__(self, num_players):
        self.deck = [Card(v, s) for s in ["Hearts", "Clubs", "Diamonds", "Spades"]
                     for v in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]
        self.num_players = num_players
        player = Hand(Card("Ace", "Hearts"), Card("2", "Clubs"))
        print(player)


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


    def add(self, card):
        if len(self.cards) == 2:
            raise Exception("Hand is full")

        self.cards.append(card)



if __name__ == "__main__":
    game = Game(4)
