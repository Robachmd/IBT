class Account:
    def __init__(self,owner,account_number,private_balance):
        self.owner= owner
        self.account_number = account_number
        self.__private_balance = private_balance
    @property
    def balance(self):
        return self.__private_balance 
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


bruk = Account("Roba", "ADB-10002938", 2000)
sami = Account("sami", "ADB-10007498", 5000)
bruk.deposit(300)
print(bruk.balance)
bruk.withdraw(800)
print(bruk.balance)

print(sami.owner)
sami.deposit(300)
print(sami.balance)
sami.withdraw(800)
print(sami.balance)
print(sami.owner)