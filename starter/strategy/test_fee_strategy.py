import unittest

from strategy.fee_strategy import (
    NoFeeStrategy,
    FixedFeeStrategy,
    PercentageFeeStrategy,
)


class TestFeeStrategy(unittest.TestCase):

    def test_no_fee_strategy(self):
        strategy = NoFeeStrategy()

        self.assertEqual(strategy.calculate_fee(100), 0)

    def test_fixed_fee_strategy(self):
        strategy = FixedFeeStrategy(5)

        self.assertEqual(strategy.calculate_fee(100), 5)

    def test_percentage_fee_strategy(self):
        strategy = PercentageFeeStrategy(10)

        self.assertEqual(strategy.calculate_fee(100), 10)

    def test_percentage_fee_strategy_different_amount(self):
        strategy = PercentageFeeStrategy(2.5)

        self.assertEqual(strategy.calculate_fee(200), 5)


if __name__ == "__main__":
    unittest.main()