# transaction.py

class Transaction:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"Transaction(${self.amount}, category='{self.category}')"

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False

        return (
            self.amount == other.amount
            and self.category == other.category
        )
