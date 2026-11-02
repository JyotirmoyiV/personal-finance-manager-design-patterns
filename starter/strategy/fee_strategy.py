from abc import ABC, abstractmethod


class FeeStrategy(ABC):
    """Interface for transaction fee calculation strategies."""

    @abstractmethod
    def calculate_fee(self, amount):
        """Calculate the fee for the supplied transaction amount."""
        pass


class NoFeeStrategy(FeeStrategy):
    """A fee strategy that does not charge a fee."""

    def calculate_fee(self, amount):
        return 0


class FixedFeeStrategy(FeeStrategy):
    """Charge the same fixed fee regardless of transaction amount."""

    def __init__(self, fee):
        self.fee = fee

    def calculate_fee(self, amount):
        return self.fee


class PercentageFeeStrategy(FeeStrategy):
    """Calculate a fee as a percentage of the transaction amount."""

    def __init__(self, percentage):
        self.percentage = percentage

    def calculate_fee(self, amount):
        return amount * self.percentage / 100
