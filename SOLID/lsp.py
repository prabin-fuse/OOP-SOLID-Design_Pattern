class Account():
    def __init__(self, balance) -> None:
        self.balance = balance

    def withdraw(self, amount):
        #no overfrafts
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

        else:
            print("Insufficient funds!")

class SavingsAccount(Account):
    pass 

class CheckingAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"The Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)


savings_account = SavingsAccount(400)
checking_account = CheckingAccount(7000, overdraft_limit=300)
perform_bank_actions(savings_account)
perform_bank_actions(checking_account)