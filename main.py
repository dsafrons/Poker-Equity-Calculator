from scoring import Score
from cards import Hand, Card
from random import choice, choices
from itertools import combinations
from time import time, sleep
import pandas as pd


class PokerGame:
    def __init__(self, num_players):
        self.deck = [Card(v, s) for s in ["Hearts", "Clubs", "Diamonds", "Spades"]
                     for v in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]
        self.hands = [Hand() for _ in range(num_players)]
        self.table = []

        self.deal_players()
        self.deal_table(3) # flop
        # self.deal_table(1) # turn
        # self.deal_table(1) # river

        # odds = pd.DataFrame(columns=["Table", "P1", "P2", "P3", "P4", "P1T", "P2T", "P3T", "P4T"])
        '''cards = [Card("Ace", "Spades"), Card("9", "Diamonds"), Card("7", "Clubs"),
                 Card("3", "Spades"), Card("Queen", "Clubs"), Card("5", "Spades"),
                 Card("King", "Hearts"), Card("Jack", "Spades"), Card("Queen", "Spades"),
                 Card("3", "Clubs"), Card("9", "Clubs")]
        self.hands = [Hand(cards[0], cards[1]), Hand(cards[2], cards[3]), Hand(cards[4], cards[5]), Hand(cards[6], cards[7])]
        self.table = [cards[8], cards[9], cards[10]]
        for card in cards:
            for c in self.deck:
                if c.value == card.value and c.suit == card.suit:
                    self.deck.remove(c)'''

        t1 = time()
        win_odds = [0, 0, 0, 0]
        tie_odds = [0, 0, 0, 0]
        for i, remaining_table in enumerate(combinations(self.deck, 2)):
            table = [*self.table, *remaining_table]

            winners = Score.determine_winner(self.hands, table)['winner-index']
            if len(winners) > 1:
                for winner in winners:
                    tie_odds[winner] += 1 / len(winners)
                pass
            else:
                win_odds[winners[0]] += 1

        end = time()-t1
            # odds.loc[i+1] = [table, entry[0], entry[1], entry[2], entry[3]]
        print(end)
        # p1 = round(odds["P1"].sum()/len(odds)*100, 2)
        # p2 = round(odds["P2"].sum()/len(odds)*100, 2)
        # p3 = round(odds["P3"].sum()/len(odds)*100, 2)
        # p4 = round(odds["P4"].sum()/len(odds)*100, 2)
        print(list(map(lambda x: round((x/820)*100, 2), win_odds)), sum(list(map(lambda x: round((x/820)*100, 2), win_odds))))
        print(list(map(lambda x: round((x/820)*100, 2), tie_odds)), sum(list(map(lambda x: round((x/820)*100, 2), tie_odds))))
        print(self.hands)
        print(self.table)

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
