class Account:
    def __init__(self,owner,account_number,private_balance):
        self.owner= owner
        self.account_number = account_number
        self.__private_balance = private_balance
        self.observers = []
        self.history=[]
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
        message= f"this transaction happen from your account type : - {self.account_type}"        
        self.notify(message)
        self.history.append(f"deposit,{amount}")
    def withdraw(self,amount):
        if amount > self.__private_balance :
            print("insuficient fund")
            return
        self.__private_balance -= amount
        self.notify(f"-you withdraw= {amount} now your balance is {self.balance}etb")
        self.history.append(f"withdraw,{amount}")

    def statement(self,account_type="main"):
        self.account_type=account_type
        message= f"this transaction happen from your account type : - {self.account_type}"
        self.notify(message)
        self.history.append(f"Account type,{self.account_type}")
        return message

    def subscribe(self,obs):
        self.observers.append(obs)
    def notify(self,event):
        for obs in self.observers:
            obs.update(event)
            
    def undo_last(self):
        return f"this is your last_transaction or undo {self.history.pop()}"
            
   

class SMSAlert:
    def update(self,event):
        print(f"[Telebirr SMS]{event}")


class SavingAccount(Account):
    def __init__(self,owner,account_number,private_balance,rate,account_type="saving account"):
        super().__init__(owner,account_number,private_balance)
        self.account_type=account_type
        self.rate=rate

    def add_intrest(self):
        self.balance += self.balance*self.rate
        
    def statement(self):
        message= f"this transaction happen from your account type : - {self.account_type}"
        self.notify(message)


class CurrentAccount(Account):
    def __init__(self,owner,account_number,private_balance,rate,account_type="current account"):
        super().__init__(owner,account_number,private_balance)
        self.account_type=account_type

    def withdraw(self,overdraft):
        self.overdraft=overdraft
        self.balance-=overdraft
        if self.overdraft > self.balance + 10000:
            print("your overdraft withdraw is unseccussful. You can only withdraw 10,000 over draft")

        else:
            self.notify(f"-you withdraw from current account = {overdraft} now your balance is {self.balance}etb")

    def statement(self):
        message= f"this transaction happen from your account type : - {self.account_type}"
        self.notify(message)
class AccountFactor:
    @staticmethod
    def create(kind,owner,account_number,private_balance,rate):
        if kind == "savingaccount":
            return SavingAccount(owner,account_number,private_balance,rate)
        if kind == "currentaccount":
            return CurrentAccount(owner,account_number,private_balance,rate)
        if kind == "account":
                    return Account(owner,account_number,private_balance)                    

class AccountRegistry:
    def __init__(self):
        self.accounts_data={}

    def add_account(self, account):
        self.accounts_data[account.account_number] = account

    def find_account(self, account_number):
        return self.accounts_data.get(account_number)
    def list_all(self):
        return sorted(self.accounts_data.keys())

current_Account=AccountFactor.create("currentaccount","Roba", "ADB-10002938", 2000,20000)

Saving_Account=AccountFactor.create("savingaccount","sami", "ADB-10007498", 5000,0.5)
main_Account=AccountFactor.create("account","sami", "ADB-10006749", 800,0.5)
accounts=[main_Account,Saving_Account,current_Account]
for i in accounts:
    i.statement()
    i.subscribe(SMSAlert())
    i.withdraw(100)
    i.account_number

    print(f"this is account balance after each class:{i.balance}")
Saving_Account.add_intrest()

print(f"this is intrest of saving account value = {Saving_Account.balance}")

registry = AccountRegistry()
registry.add_account(main_Account)
registry.add_account(current_Account)
registry.add_account(Saving_Account)
findAccount=registry.find_account("ADB-10007498")
findAccount.deposit(500)
findAccount.withdraw(300)
print(findAccount.statement())
print(registry.list_all())

print(findAccount.history)
print(findAccount.undo_last())
print(findAccount.owner)
print(findAccount.balance)
print(findAccount.owner)
print(findAccount.account_type)