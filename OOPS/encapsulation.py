class BankAccount:
    def __init__(self, balance) -> None:
        self._balance = balance

        def deposit(amount):
            if amount > 0: self._balance += amount

        def withdraw(self, amount):
            if amount > 0 and amount <= self._balance:
                self._balance -= amount

        def get_balance(self): return self._balance


account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Account Balance:", account.get_balance())  # Output: 1300

# Real-Time Use Case: A banking system where balance is encapsulated within the BankAccount class with restricted access.