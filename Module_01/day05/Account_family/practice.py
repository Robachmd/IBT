from abc import abstractmethod,ABC
class Vehicle(ABC):
    def __init__(self,make,model):
        self.make=make
        self.model = model
    def describe(self):
        print(f"{self.make} and {self.model}")
    @abstractmethod
    def wheels(self):
        pass
class Car(Vehicle):
    pass
    def wheels(self,number=9):
        self.number =number
        print(self.number)
class Truck(Vehicle):
    def __init__(self,make,model,capacity):
        super().__init__(make,model)
        self.capacity = capacity
    def describe(self):
        print(f"my {self.make}, {self.model},{self.capacity}")
    def wheels(self,number=8):
        self.number=number
        print(self.number)
# v1 = Vehicle("Ford", "Focus")
c1 = Car("Toyota", "Corolla")
t1 = Truck("Volvo", "FH16", 20)
# list_vehicle=[v1,c1,t1]
list_vehicle=[c1,t1]

for i in list_vehicle:
    i.describe()
    i.wheels()