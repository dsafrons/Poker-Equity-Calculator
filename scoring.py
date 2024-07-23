"""def determine_winner(hands, table):
    # classifies all the hands with all the tied comparisons in order after the classification
    # compare the classifications first by rank of hand then by the tie comparison
    # return index of the winning classification in hands
    pass


def classify_hand(hand, table):
    pass


def compare_classification(c1, c2):
    pass"""
from cards import Hand


class Score:
    @staticmethod
    def convert_to_all_cards(hand, table):
        all_cards = [hand.cards[0], hand.cards[1]]
        for card in table:
            all_cards.append(card)

        return all_cards

    @staticmethod
    def greatest_to_least(cards):
        values = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        ordered = []

        for val in values:
            for card in cards:
                if card.value == val:
                    ordered.append(card)

        return ordered

    @staticmethod
    def is_royal_flush(hand, table):
        all_cards = Score.convert_to_all_cards(hand, table)
        royal_flush_set = {"Ace", "King", "Queen", "Jack", "10"}
        suits = {"Hearts": set(), "Clubs": set(), "Diamonds": set(), "Spades": set()}

        for card in all_cards:
            if card.value in royal_flush_set:
                suits[card.suit].add(card.value)

        for suit, values in suits.items():
            if values == royal_flush_set:
                return True

        return False

    @staticmethod
    def is_straight_flush(hand, table):
        is_flush = Score.is_flush(hand, table)
        if is_flush:
            return Score.is_straight(Hand(is_flush[1][0], is_flush[1][1]), is_flush[1][2:])

    @staticmethod
    def is_four_of_a_kind(hand, table):
        all_cards = Score.convert_to_all_cards(hand, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in all_cards:
            values[card.value].append(card)
            if len(values[card.value]) == 4:
                return card

        return False

    @staticmethod
    def is_full_house(hand, table):
        three_of_a_kind = Score.is_three_of_a_kind(hand, table)
        one_pair = Score.is_one_pair(hand, table)
        if three_of_a_kind and one_pair:
            return [three_of_a_kind, one_pair[0][0]]

    @staticmethod
    def is_flush(hand, table):
        all_cards = Score.convert_to_all_cards(hand, table)
        suits = {"Hearts": [], "Clubs": [], "Diamonds": [], "Spades": []}

        for card in all_cards:
            suits[card.suit].append(card)

        for suit, cards in suits.items():
            if len(cards) >= 5:
                return [suit, Score.greatest_to_least(cards)]

        return False

    @staticmethod
    def is_straight(hand, table):
        all_cards = Score.convert_to_all_cards(hand, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": [], "Ace2": []}

        for card in all_cards:
            if card.value == "Ace":
                values["Ace2"].append(card)
            values[card.value].append(card)

        streak = 0
        streak_card = None
        for value, cards in values.items():
            if cards:
                if streak == 0:
                    streak_card = cards[0]
                streak += 1
            else:
                streak = 0
                streak_card = None

            if streak == 5:
                return streak_card

        return False

    @staticmethod
    def is_three_of_a_kind(hand, table):
        all_cards = Score.convert_to_all_cards(hand, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in all_cards:
            values[card.value].append(card)

        for cards in values.values():
            if len(cards) == 3:
                return cards[0]

        return False

    @staticmethod
    def is_two_pair(hand, table):
        all_cards = Score.convert_to_all_cards(hand, table)
        one_pair = Score.is_one_pair(hand, table)
        if one_pair:
            two_pair = Score.is_one_pair(Hand(one_pair[1][0], one_pair[1][1]), one_pair[1][2:])
            if two_pair:
                return [Score.greatest_to_least([one_pair[0][0], two_pair[0][0]]),
                        Score.greatest_to_least([c for c in all_cards if c not in one_pair[0] and c not in two_pair[0]])]

        return False

    @staticmethod
    def is_one_pair(hand, table):
        all_cards = Score.convert_to_all_cards(hand, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in all_cards:
            values[card.value].append(card)

        for cards in values.values():
            if len(cards) >= 2:
                return [cards, Score.greatest_to_least([c for c in all_cards if c not in cards])]

        return False

    @staticmethod
    def is_high_card(hand, table):
        return Score.greatest_to_least(Score.convert_to_all_cards(hand, table))
