"""This module serves as the entry point for the program."""

from balance.balance import Balance
from balance.balance_observer import (
    LowBalanceAlertObserver,
    PrintObserver,
)
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_adapter import TransactionAdapter
from transaction.external_income_transaction import ExternalFreelanceIncome
from strategy.fee_strategy import PercentageFeeStrategy


def main():
    print("Adding transactions...")

    # Singleton Pattern
    balance = Balance.get_instance()
    balance.reset()

    # Observer Pattern
    print_observer = PrintObserver()
    low_balance_observer = LowBalanceAlertObserver(threshold=50)

    balance.register_observer(print_observer)
    balance.register_observer(low_balance_observer)

    # Create standard transactions
    transactions = [
        Transaction(100, TransactionCategory.INCOME),
        Transaction(50, TransactionCategory.EXPENSE),
        Transaction(200, TransactionCategory.INCOME),
        Transaction(75, TransactionCategory.EXPENSE),
    ]

    # Adapter Pattern
    freelance_income = ExternalFreelanceIncome(
        1200,
        "INV-98765",
        "Mobile App Project",
    )

    adapter = TransactionAdapter(freelance_income)
    adapted_transaction = adapter.to_transaction()

    all_transactions = transactions + [adapted_transaction]

    # Apply all transactions
    for transaction in all_transactions:
        balance.apply_transaction(transaction)

    # Strategy Pattern
    fee_strategy = PercentageFeeStrategy(2.5)
    freelance_fee = fee_strategy.calculate_fee(
        freelance_income.amount
    )

    print(f"\nFreelance transaction fee: ${freelance_fee:.2f}")
    print(balance.summary())


if __name__ == "__main__":
    main()