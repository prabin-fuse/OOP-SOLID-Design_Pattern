class BankAccount:

    def __init__(self, account_num, balance, account_type):
        self.account_num = account_num
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print("The desctuctor is deleting BankAccount.")
    
    def display(self):
        return "Account Number : {}, Balance : {}, Account Type : {}".format(self.account_num, self.balance, self. account_type)
    


class Customer:
    
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bankaccount = None

    def __del__(self):
        print("The destructor is deleting Customer.")
    
    def add_bank(self, account):
        self.bankaccount = account

    def display(self):
        return "Name : {}, Age : {}, Address : {}".format(self.name, self.age, self.address)


###main testing:

bankacc1  = BankAccount(114520, 45000,"Saving")
bankacc2  = BankAccount(114521, 780000,"Current")

customer1 = Customer("Prabin", 24, "Kathmandu")
customer1.add_bank(bankacc1)

print(bankacc1.display())
print(customer1.display())
