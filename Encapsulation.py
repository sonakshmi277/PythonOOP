class BankAccount:
    def __init__(self, owner, balance,pt):
        self.owner = owner           # Public attribute  Accessible from anywhere.
        self.__balance = balance     # Private attribute  Accessible only within the class.
        self._pt=pt                 #protected attribute  Accessible within the class and its subclasses.

    # Public method to display account info
    def show_account(self):
        print(f"Account owner: {self.owner}")
        print(f"Balance: {self.__balance}")

    # Getter for private attribute
    def get_balance(self):
        return self.__balance

    # Setter for private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid or insufficient funds for withdrawal.")

acc = BankAccount("Alice", 1000)

# Access public data
print(acc.owner)       # ✅ prints Alice

# Try to access private data directly
# print(acc.__balance) # 🚫 AttributeError

# Use getter & public methods
print(acc.get_balance())  # ✅ prints 1000

acc.deposit(500)          # ✅ adds money
acc.withdraw(300)         # ✅ subtracts money
acc.show_account()        # ✅ prints all info
