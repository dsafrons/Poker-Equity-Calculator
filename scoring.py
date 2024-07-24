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
from collections import OrderedDict
import numpy as np


class ScoreHelper:
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
        all_cards = ScoreHelper.convert_to_all_cards(hand, table)
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
        is_flush = ScoreHelper.is_flush(hand, table)

        if is_flush:
            return ScoreHelper.is_straight(Hand(is_flush[0], is_flush[1]), is_flush[2:])

        return False

    @staticmethod
    def is_four_of_a_kind(hand, table):
        all_cards = ScoreHelper.convert_to_all_cards(hand, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in all_cards:
            values[card.value].append(card)

            if len(values[card.value]) == 4:
                return card

        return False

    @staticmethod
    def is_full_house(hand, table):
        all_cards = ScoreHelper.convert_to_all_cards(hand, table)
        three_of_a_kind = ScoreHelper.is_three_of_a_kind(hand, table)

        if three_of_a_kind:
            rest = [c for c in all_cards if c not in three_of_a_kind]
            one_pair = ScoreHelper.is_one_pair(Hand(rest[0], rest[1]), rest[2:])

            if one_pair:
                return [three_of_a_kind[0], one_pair[0][0]]

        return False

    @staticmethod
    def is_flush(hand, table):
        all_cards = ScoreHelper.convert_to_all_cards(hand, table)
        suits = {"Hearts": [], "Clubs": [], "Diamonds": [], "Spades": []}

        for card in all_cards:
            suits[card.suit].append(card)

        for suit, cards in suits.items():
            if len(cards) >= 5:
                return ScoreHelper.greatest_to_least(cards)

        return False

    @staticmethod
    def is_straight(hand, table):
        all_cards = ScoreHelper.convert_to_all_cards(hand, table)
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
        all_cards = ScoreHelper.convert_to_all_cards(hand, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in all_cards:
            values[card.value].append(card)

        for cards in values.values():
            if len(cards) == 3:
                return cards

        return False

    @staticmethod
    def is_two_pair(hand, table):
        all_cards = ScoreHelper.convert_to_all_cards(hand, table)
        one_pair = ScoreHelper.is_one_pair(hand, table)

        if one_pair:
            two_pair = ScoreHelper.is_one_pair(Hand(one_pair[1][0], one_pair[1][1]), one_pair[1][2:])

            if two_pair:
                return [ScoreHelper.greatest_to_least([one_pair[0][0], two_pair[0][0]]),
                        ScoreHelper.greatest_to_least([c for c in all_cards if c not in one_pair[0]
                                                       and c not in two_pair[0]])]

        return False

    @staticmethod
    def is_one_pair(hand, table):
        all_cards = ScoreHelper.convert_to_all_cards(hand, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in all_cards:
            values[card.value].append(card)

        for cards in values.values():
            if len(cards) >= 2:
                return [cards, ScoreHelper.greatest_to_least([c for c in all_cards if c not in cards])]

        return False

    @staticmethod
    def is_high_card(hand, table):
        return ScoreHelper.greatest_to_least(ScoreHelper.convert_to_all_cards(hand, table))


class Score:
    @staticmethod
    def classify_hand(hand, table):
        if ScoreHelper.is_royal_flush(hand, table):
            return {"rank": 1, "tie-breaker": [14]}

        if straight_flush := ScoreHelper.is_straight_flush(hand, table):
            return {"rank": 2, "tie-breaker": [straight_flush.num_value]}

        if four_of_a_kind := ScoreHelper.is_four_of_a_kind(hand, table):
            return {"rank": 3, "tie-breaker": [four_of_a_kind.num_value]}

        if full_house := ScoreHelper.is_full_house(hand, table):
            return {"rank": 4, "tie-breaker": [*map(lambda c: c.num_value, full_house)]}

        if flush := ScoreHelper.is_flush(hand, table):
            return {"rank": 5, "tie-breaker": [*map(lambda c: c.num_value, flush)]}

        if straight := ScoreHelper.is_straight(hand, table):
            return {"rank": 6, "tie-breaker": [straight.num_value]}

        if three_of_a_kind := ScoreHelper.is_three_of_a_kind(hand, table):
            return {"rank": 7, "tie-breaker": [three_of_a_kind[0].num_value]}

        if two_pair := ScoreHelper.is_two_pair(hand, table):
            return {"rank": 8, "tie-breaker": [*map(lambda c: c.num_value, two_pair[0]),
                                               *map(lambda c: c.num_value, two_pair[1])]}

        if one_pair := ScoreHelper.is_one_pair(hand, table):
            return {"rank": 9, "tie-breaker": [one_pair[0][0].num_value, *map(lambda c: c.num_value, one_pair[1])]}

        high_card = ScoreHelper.is_high_card(hand, table)
        return {"rank": 10, "tie-breaker": [*map(lambda c: c.num_value, high_card)]}

    @staticmethod
    def determine_winner(hands, table):
        rank_to_hand = {1: "Royal Flush", 2: "Straight Flush", 3: "Four of a Kind", 4: "Full House", 5: "Flush",
                        6: "Straight", 7: "Three of a Kind", 8: "Two Pair", 9: "One Pair", 10: "High Card"}
        scores = {}

        for i in range(len(hands)):
            scores[i] = Score.classify_hand(hands[i], table)

        ordered_scores = dict(sorted(scores.items(), key=lambda item: item[1]['rank']))
        highest_score = 10
        for key, value in dict(ordered_scores).items():
            if value['rank'] <= highest_score:
                highest_score = value['rank']
            else:
                del ordered_scores[key]

        if len(ordered_scores) > 1:
            ordered_scores = dict(sorted(ordered_scores.items(), key=lambda item: item[1]['tie-breaker'], reverse=True))
            best_tiebreaker = list(ordered_scores.values())[0]['tie-breaker']
            tie_idx = [idx for idx, hand in reversed(ordered_scores.items()) if hand['tie-breaker'] == best_tiebreaker]

            if len(tie_idx) > 1:
                return {"winner-index": sorted(tie_idx),
                        "hand": rank_to_hand[list(ordered_scores.values())[0]['rank']]}

        return {"winner-index": list(ordered_scores.keys())[0],
                "hand": rank_to_hand[list(ordered_scores.values())[0]['rank']]}
