Design Patterns Reflection
This project implements four object-oriented design patterns: Singleton, Adapter, Observer, and Strategy.

Singleton Pattern
The Balance class uses the Singleton pattern so that the finance manager has one shared balance instance across the application.

This avoids different parts of the application maintaining separate balance values and provides a single source of truth.

A trade-off is that Singleton introduces shared state, so tests must reset the balance to ensure they remain independent.

Adapter Pattern
The TransactionAdapter converts ExternalFreelanceIncome objects into the standard Transaction representation used by the finance manager.

The external freelance model contains fields such as invoice ID and description, while the application requires an amount and transaction category. The adapter isolates this conversion logic from the core transaction and balance classes.

This improves flexibility because other external transaction formats could be supported using additional adapters without changing the core model.

Observer Pattern
The Balance acts as the subject and notifies registered observers whenever a transaction changes the balance.

Two observers are implemented:

PrintObserver prints the updated balance after a transaction.
LowBalanceAlertObserver detects when the balance falls below a configured threshold.
The Observer pattern keeps notification behaviour separate from the Balance calculation logic. New observers can therefore be introduced without changing the transaction-processing code.

The trade-off is additional coordination between the subject and registered observers, and observer state must be considered when using a Singleton.

Strategy Pattern
I chose the Strategy pattern for transaction fee calculations.

The finance manager provides:

NoFeeStrategy
FixedFeeStrategy
PercentageFeeStrategy
Each strategy implements a different fee calculation while exposing the same calculate_fee() operation.

The Strategy pattern fits the application because transaction fees can vary depending on the type or source of a transaction. For example, the application demonstration calculates a 2.5% fee for freelance income.

This improves flexibility because fee algorithms can be changed without modifying Transaction or Balance. It improves testability because each strategy can be tested independently, and it improves scalability because new fee strategies can be introduced without changing existing strategies.

The trade-off is that the application contains more classes than a simple conditional-based implementation, but this separation becomes valuable as the number of fee policies grows.

Testing
The project contains unit tests for:

Balance and Singleton behaviour
Transaction behaviour
Transaction Adapter
Balance Observers
Fee Strategies
All 18 tests pass.

Run the tests with:

python3 -m unittest \
  balance/test_balance.py \
  balance/test_balance_observer.py \
  transaction/test_transaction.py \
  transaction/test_transaction_adapter.py \
  strategy/test_fee_strategy.py -v
Running the Application
Run:

python3 main.py