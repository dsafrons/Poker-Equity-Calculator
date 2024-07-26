from scoring import Score
from cards import Hand, Card
from random import choice, choices
from itertools import combinations


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

        win, tie = self.calculate_odds()
        print(self.hands)
        print(self.table)
        print(win)
        print(tie)

    def calculate_odds(self):
        win_odds = [0] * len(self.hands)
        tie_odds = [0] * len(self.hands)
        i = 0

        for remaining_table in combinations(self.deck, 5 - len(self.table)):
            table = [*self.table, *remaining_table]

            winners = Score.determine_winner(self.hands, table)['winner-index']
            if len(winners) > 1:
                for winner in winners:
                    tie_odds[winner] += 1 / len(winners)
            else:
                win_odds[winners[0]] += 1

            i += 1

        return (list(map(lambda odd: round((odd/i)*100, 2), win_odds)),
                list(map(lambda odd: round((odd/i)*100, 2), tie_odds)))

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
