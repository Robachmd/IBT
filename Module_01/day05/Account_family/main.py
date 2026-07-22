class Account:
    def __init__(self,owner,account_number,private_balance):
        self.owner= owner
        self.account_number = account_number
        self.__private_balance = private_balance
    @property
    def balance(self):
        return self.__private_balance 
    @balance.setter
    def balance(self,balance):
        self.__private_balance = balance
    def deposit(self,amount):
        if amount < 0:
            raise ValueError("invalid input")
            return 
        self.__private_balance += amount
    def withdraw(self,amount):
        if amount > self.__private_balance :
            print("insuficient fund")
            return
        self.__private_balance -= amount
    def statement(self,account_type="main"):
        self.account_type=account_type
        print(f"this account type is - {self.account_type}")
class SavingAccount(Account):
    def __init__(self,owner,account_number,private_balance,rate,account_type="saving account"):
        super().__init__(owner,account_number,private_balance)
        self.account_type=account_type
        self.rate=rate

    def add_intrest(self):
        self.balance += self.balance*self.rate
        
    def statement(self):
        print(f"this account type is - {self.account_type}")
class CurrentAccount(Account):
    def __init__(self,owner,account_number,private_balance,rate,account_type="current account"):
        super().__init__(owner,account_number,private_balance)
        self.account_type=account_type

    def withdraw(self,overdraft):
        self.overdraft=overdraft

        if self.overdraft > self.balance + 10000:
            print("your overdraft withdraw is unseccussful. You can only withdraw 10,000 over draft")

        else:
            print(f"this is over draft value of saving account = {self.overdraft - self.balance}")

    def statement(self):
        print(f"this account type is - {self.account_type}")
   
main_account=Account("Roba", "ADB-10002938", 2000)
Saving_Account=SavingAccount("sami", "10007498", 5000,0.5)
current_Account=CurrentAccount("sami", "ADB-10007498", 800,0.5)
accounts=[main_account,Saving_Account,current_Account]
for i in accounts:
    i.statement()

    print(f"this is account balance after each class:{i.balance}")
    i.withdraw(20000)
Saving_Account.add_intrest()

print(f"this is intrest of saving account value = {Saving_Account.balance}")
