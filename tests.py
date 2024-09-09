from cards import Card, Hole
from scoring import Score, ScoreHelper
from time import perf_counter
from functools import wraps


class Test:
    @staticmethod
    def timeit(func):
        @wraps(func)
        def timeit_wrapper(*args, **kwargs):
            start_time = perf_counter()
            result = func(*args, **kwargs)
            end_time = perf_counter()
            total_time = end_time - start_time
            print('--------------------')
            print(f'{total_time:.8f}s')
            return result

        return timeit_wrapper

    @staticmethod
    @timeit
    def test_royal_flush():
        hole = Hole(Card('10', 'Hearts'), Card('Jack', 'Hearts'))
        table = [Card('King', 'Hearts'), Card('Queen', 'Hearts'), Card('3', 'Hearts'),
                 Card('Ace', 'Hearts'), Card('5', 'Spades')]

        return ScoreHelper.is_royal_flush(hole, table)

    @staticmethod
    @timeit
    def test_flush():
        hole = Hole(Card('7', 'Hearts'), Card('Ace', 'Hearts'))
        table = [Card('10', 'Hearts'), Card('9', 'Hearts'), Card('Queen', 'Hearts'),
                 Card('Ace', 'Spades'), Card('6', 'Hearts')]

        return ScoreHelper.is_flush(hole, table)

    @staticmethod
    @timeit
    def test_three_of_a_kind():
        hole = Hole(Card('King', 'Spades'), Card('2', 'Diamonds'))
        table = [Card('5', 'Clubs'), Card('10', 'Diamonds'), Card('Ace', 'Hearts'),
                 Card('2', 'Clubs'), Card('2', 'Spades')]

        return ScoreHelper.is_three_of_a_kind(hole, table)

    @staticmethod
    @timeit
    def test_straight():
        hole = Hole(Card('6', 'Spades'), Card('5', 'Diamonds'))
        table = [Card('4', 'Clubs'), Card('7', 'Diamonds'), Card('Queen', 'Hearts'),
                 Card('Jack', 'Hearts'), Card('3', 'Spades')]

        return ScoreHelper.is_straight(hole, table)

    @staticmethod
    @timeit
    def test_straight_flush():
        hole = Hole(Card('King', 'Spades'), Card('Queen', 'Spades'))
        table = [Card('Jack', 'Spades'), Card('9', 'Spades'), Card('3', 'Spades'),
                 Card('2', 'Spades'), Card('10', 'Spades')]

        return ScoreHelper.is_straight_flush(hole, table)

    @staticmethod
    @timeit
    def test_four_of_a_kind():
        hole = Hole(Card('Ace', 'Hearts'), Card('Ace', 'Diamonds'))
        table = [Card('5', 'Clubs'), Card('10', 'Diamonds'), Card('7', 'Hearts'),
                 Card('Ace', 'Clubs'), Card('Ace', 'Spades')]

        return ScoreHelper.is_four_of_a_kind(hole, table)

    @staticmethod
    @timeit
    def test_one_pair():
        hole = Hole(Card('Ace', 'Hearts'), Card('2', 'Diamonds'))
        table = [Card('5', 'Clubs'), Card('10', 'Diamonds'), Card('7', 'Hearts'),
                 Card('2', 'Clubs'), Card('9', 'Spades')]

        return ScoreHelper.is_one_pair(hole, table)

    @staticmethod
    @timeit
    def test_two_pair():
        hole = Hole(Card('Queen', 'Hearts'), Card('8', 'Diamonds'))
        table = [Card('3', 'Spades'), Card('2', 'Diamonds'), Card('7', 'Hearts'),
                 Card('2', 'Clubs'), Card('Queen', 'Spades')]

        return ScoreHelper.is_two_pair(hole, table)

    @staticmethod
    @timeit
    def test_full_house():
        hole = Hole(Card('Queen', 'Hearts'), Card('Ace', 'Diamonds'))
        table = [Card('Ace', 'Spades'), Card('9', 'Diamonds'), Card('7', 'Hearts'),
                 Card('7', 'Clubs'), Card('7', 'Spades')]

        return ScoreHelper.is_full_house(hole, table)

    @staticmethod
    @timeit
    def test_high_card():
        hole = Hole(Card('Queen', 'Hearts'), Card('2', 'Diamonds'))
        table = [Card('10', 'Spades'), Card('9', 'Diamonds'), Card('7', 'Hearts'),
                 Card('3', 'Clubs'), Card('4', 'Spades')]

        return ScoreHelper.is_high_card(hole, table)
