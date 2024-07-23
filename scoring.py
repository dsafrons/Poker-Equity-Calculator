from cards import Hand


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
        royal_flush = ScoreHelper.is_royal_flush(hand, table)
        straight_flush = ScoreHelper.is_straight_flush(hand, table)
        four_of_a_kind = ScoreHelper.is_four_of_a_kind(hand, table)
        full_house = ScoreHelper.is_full_house(hand, table)
        flush = ScoreHelper.is_flush(hand, table)
        straight = ScoreHelper.is_straight(hand, table)
        three_of_a_kind = ScoreHelper.is_three_of_a_kind(hand, table)
        two_pair = ScoreHelper.is_two_pair(hand, table)
        one_pair = ScoreHelper.is_one_pair(hand, table)
        high_card = ScoreHelper.is_high_card(hand, table)

        if royal_flush:
            return {"rank": 1}
        if straight_flush:
            return {"rank": 2, "tie-breaker": straight_flush}
        if four_of_a_kind:
            return {"rank": 3, "tie-breaker": four_of_a_kind}
        if full_house:
            return {"rank": 4, "tie-breaker": full_house}
        if flush:
            return {"rank": 5, "tie-breaker": flush}
        if straight:
            return {"rank": 6, "tie-breaker": straight}
        if three_of_a_kind:
            return {"rank": 7, "tie-breaker": three_of_a_kind[0]}
        if two_pair:
            return {"rank": 8, "tie-breaker": two_pair}
        if one_pair:
            return {"rank": 9, "tie-breaker": [one_pair[0][0], one_pair[1]]}

        return {"rank": 10, "tie-breaker": high_card}
