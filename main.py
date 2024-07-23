from scoring import Score
from cards import Hand, Card
from random import choice, choices


class PokerGame:
    def __init__(self, num_players):
        self.deck = [Card(v, s) for s in ["Hearts", "Clubs", "Diamonds", "Spades"]
                     for v in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]
        self.hands = [Hand() for _ in range(num_players)]
        self.table = []

        self.deal_players()
        self.deal_table(3) # flop
        self.deal_table(1) # turn
        self.deal_table(1) # river

    def deal_players(self):
        for hand in self.hands:
            cards = choices(self.deck, k=2)
            hand.add(cards[0], cards[1])
            self.deck = [c for c in self.deck if c not in cards]

    def deal_table(self, num_cards):
        for i in range(num_cards):
            card = choice(self.deck)
            self.table.append(card)
            self.deck.remove(card)


if __name__ == "__main__":
    poker_game = PokerGame(4)
