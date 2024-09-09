from cards import *


class ScoreHelper:
    @staticmethod
    def convert_to_all_cards(hole, table):
        return [*hole.cards, *table]

    @staticmethod
    def cards_num_value(cards):
        return [*map(lambda c: c.num_value, cards)]

    @staticmethod
    def keep_cards_by_suit(all_cards, suit):
        return [card for card in all_cards if card.suit == suit]

    @staticmethod
    def keep_cards_except_value(all_cards, value, value2=None):
        return [card for card in all_cards if card.value not in [value, value2]]

    @staticmethod
    def greatest_to_least(cards):
        return sorted(cards, key=lambda c: c.num_value, reverse=True)

    @staticmethod
    def is_royal_flush(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        royal_flush_values = ["Ace", "King", "Queen", "Jack", "10"]
        suits = {"Hearts": 0, "Clubs": 0, "Diamonds": 0, "Spades": 0}

        for card in all_cards:
            if card.value in royal_flush_values:
                suits[card.suit] += 1

        for suit, num_cards in suits.items():
            if num_cards == 5:
                return [Card(value, suit) for value in royal_flush_values]

    @staticmethod
    def is_straight_flush(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        suits = {"Hearts": [], "Clubs": [], "Diamonds": [], "Spades": []}

        for card in all_cards:
            suits[card.suit].append(card)

        for cards in suits.values():
            if len(cards) >= 5:
                return ScoreHelper.is_straight(Hole(cards[0], cards[1]), cards[2:])

        return False

    @staticmethod
    def is_four_of_a_kind(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in all_cards:
            values[card.value].append(card)

            if len(values[card.value]) == 4:
                return [*values[card.value],
                        ScoreHelper.greatest_to_least(ScoreHelper.keep_cards_except_value(all_cards, card.value))[0]]

        return False

    @staticmethod
    def is_full_house(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        three_of_a_kind = ScoreHelper.is_three_of_a_kind(hole, table)

        if three_of_a_kind:
            rest = ScoreHelper.keep_cards_except_value(all_cards, three_of_a_kind[0].value)
            one_pair = ScoreHelper.is_one_pair(Hole(rest[0], rest[1]), rest[2:])

            if one_pair:
                return [*three_of_a_kind[:3], *one_pair[:2]]

        return False

    @staticmethod
    def is_flush(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        suits = {"Hearts": [], "Clubs": [], "Diamonds": [], "Spades": []}

        for card in ScoreHelper.greatest_to_least(all_cards):
            suits[card.suit].append(card)

            if len(suits[card.suit]) == 5:
                return suits[card.suit]

        return False

    @staticmethod
    def is_straight(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": [], "Ace2": []}

        for card in all_cards:
            if card.value == "Ace":
                values["Ace2"].append(card)

            values[card.value].append(card)

        streak_cards = []
        for value, cards in values.items():
            if len(cards) > 0:
                streak_cards.append(cards[0])
            else:
                streak_cards = []

            if len(streak_cards) == 5:
                return streak_cards

        return False

    @staticmethod
    def is_three_of_a_kind(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in ScoreHelper.greatest_to_least(all_cards):
            values[card.value].append(card)

            if len(values[card.value]) == 3:
                return [*values[card.value],
                        *ScoreHelper.greatest_to_least(ScoreHelper.keep_cards_except_value(all_cards, card.value))[:2]]

        return False

    @staticmethod
    def is_two_pair(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        values_with_pairs = []
        for card in ScoreHelper.greatest_to_least(all_cards):
            values[card.value].append(card)

            if len(values[card.value]) == 2:
                values_with_pairs.append(card.value)

        if len(values_with_pairs) >= 2:
            return [*values[values_with_pairs[0]], *values[values_with_pairs[1]],
                    ScoreHelper.greatest_to_least(ScoreHelper.keep_cards_except_value(
                        all_cards, values_with_pairs[0], values_with_pairs[1]))[0]]

        return False

    @staticmethod
    def is_one_pair(hole, table):
        all_cards = ScoreHelper.convert_to_all_cards(hole, table)
        values = {"Ace": [], "King": [], "Queen": [], "Jack": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [],
                  "4": [], "3": [], "2": []}

        for card in all_cards:
            values[card.value].append(card)

        for value, cards in values.items():
            if len(cards) >= 2:
                return [*cards[:2],
                        *ScoreHelper.greatest_to_least(ScoreHelper.keep_cards_except_value(all_cards, value))[:3]]

        return False

    @staticmethod
    def is_high_card(hole, table):
        return ScoreHelper.greatest_to_least(ScoreHelper.convert_to_all_cards(hole, table))[:5]


class Score:
    @staticmethod
    def classify_hand(hole, table):
        if royal_flush := ScoreHelper.is_royal_flush(hole, table):
            return {"rank": "Royal Flush", "hand": royal_flush}

        if straight_flush := ScoreHelper.is_straight_flush(hole, table):
            return {"rank": "Straight Flush", "hand": straight_flush}

        if four_of_a_kind := ScoreHelper.is_four_of_a_kind(hole, table):
            return {"rank": "Four of a Kind", "hand": four_of_a_kind}

        if full_house := ScoreHelper.is_full_house(hole, table):
            return {"rank": "Full House", "hand": full_house}

        if flush := ScoreHelper.is_flush(hole, table):
            return {"rank": "Flush", "hand": flush}

        if straight := ScoreHelper.is_straight(hole, table):
            return {"rank": "Straight", "hand": straight}

        if three_of_a_kind := ScoreHelper.is_three_of_a_kind(hole, table):
            return {"rank": "Three of a Kind", "hand": three_of_a_kind}

        if two_pair := ScoreHelper.is_two_pair(hole, table):
            return {"rank": "Two Pair", "hand": two_pair}

        if one_pair := ScoreHelper.is_one_pair(hole, table):
            return {"rank": "One Pair", "hand": one_pair}

        return {"rank": "High Card", "hand": ScoreHelper.is_high_card(hole, table)}

    @staticmethod
    def determine_winner(holes, table):
        rank_to_num = {"Royal Flush": 1, "Straight Flush": 2, "Four of a Kind": 3, "Full House": 4, "Flush": 5,
                       "Straight": 6, "Three of a Kind": 7, "Two Pair": 8, "One Pair": 9, "High Card": 10}

        hands = {hole_idx: Score.classify_hand(hole, table) for hole_idx, hole in enumerate(holes)}

        max_rank_num = min([rank_to_num[hand_info['rank']] for hand_info in hands.values()])
        filtered_hands = {k: v for k, v in hands.items() if rank_to_num[v['rank']] == max_rank_num}

        # If there is more than 1 of the same ranked hand then sort by the hand kickers which are the card values
        if len(filtered_hands) > 1:
            hand_kicker = max([[c.num_value for c in hand_info['hand']] for hand_info in filtered_hands.values()])
            filtered_hands = {k: v for k, v in filtered_hands.items() if [c.num_value for c in v['hand']] == hand_kicker}

        # If there is a tie
        if len(filtered_hands) > 1:
            tie_idx = sorted(list(filtered_hands.keys()))
            hands = [v['hand'] for v in filtered_hands.values()]
            return {'winner-index': tie_idx, 'rank': list(filtered_hands.values())[0]['rank'], 'hand': hands}

        return {'winner-index': list(filtered_hands.keys()), 'rank': list(filtered_hands.values())[0]['rank'],
                'hand': list(filtered_hands.values())[0]['hand']}
