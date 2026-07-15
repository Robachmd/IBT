# # exercise 1
# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.auhtor = author
#         self.pages = pages
#     def describe(self):
#         print(self.title)
#         print(self.auhtor)
#         print(self.pages)
# power = Book("power","alakewum",330)

# power.describe()

class Product:
    
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity
    @property
    def quantity(self):
        if self.__quantity < 0 :
            raise ValueError("can't be less than 0")
        return self.__quantity

    def restock(self,amount):
        if self.__quantity < 0:
            raise ValueError("invalid error")
            return
        self.__quantity+=amount
    
    def sell(self,amount):
        if amount < 0:
            raise ValueError("insufficient product")
        else:
            self.__quantity -= amount
   
prod1=Product("byd",200000,50)
prod2=Product("lexus",50000,70)
prod3=Product("ford",70000,20)
prod1.sell(5)
prod2.sell(6)
prod3.sell(6)
print("this is for sell")
print(prod1.quantity)
print(prod2.quantity)
print(prod3.quantity)
prod1.restock(5)
prod2.restock(6)
prod3.restock(6)
print("this is for restock")
print(prod1.quantity)
print(prod2.quantity)
print(prod3.quantity)