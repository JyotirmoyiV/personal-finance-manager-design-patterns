# balance.py

from transaction.transaction_category import TransactionCategory


class Balance:
    """Singleton to track the balance."""

    _instance = None

    def __init__(self):
        """Initialise the balance and observer list."""
        self._balance = 0.0
        self._observers = []

    @classmethod
    def get_instance(cls):
        """Return the singleton Balance instance."""
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def reset(self):
        """Reset the net balance to zero."""
        self._balance = 0.0

    def add_income(self, amount):
        """Add income to the balance."""
        self._balance += amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self._balance -= amount

    def apply_transaction(self, transaction):
        """Apply a transaction and notify observers."""

        if transaction.category == TransactionCategory.INCOME:
            self.add_income(transaction.amount)

        elif transaction.category == TransactionCategory.EXPENSE:
            self.add_expense(transaction.amount)

        else:
            raise ValueError("Invalid transaction category")

        self.notify_observers(transaction)

    def get_balance(self):
        """Return the current balance."""
        return self._balance

    def summary(self):
        """Return a summary of the current balance."""
        return f"Net balance: {self._balance}"

    def register_observer(self, observer):
        """Register an observer for balance changes."""
        if observer not in self._observers:
            self._observers.append(observer)

    def notify_observers(self, transaction):
        """Notify registered observers of a balance change."""
        for observer in self._observers:
            observer.update(self, transaction)
