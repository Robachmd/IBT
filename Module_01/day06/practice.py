Q1
class BuildReport:
    def __init__(self,name,studentId):
        self.name=name
        self.studentId=studentId
        self.mark=[]
        self.subjects=[]
        
    def subject(self,subject,mark):
        self.mark.append(mark)
        self.subjects.append(subject)
    def average(self):
        avg=sum(self.mark)/len(self.mark)
        return avg
    def grade(self):
        print(f"{self.name}:{self.studentId} get ")

        if self.average() > 50:
            return "passed"
        else:
            return "failed"
class SavesReport:
    def savereport(self,report):
        with open("saverport.txt","w") as f:
            f.write(f"{report.name},{report.studentId}\n ")
            f.write("Your grade report\n")

            for subject, mark in zip(report.subjects, report.mark):

                f.write(f"{subject}={mark}\n ")
                
            f.write(f"your average is :{report.average()}")
            f.write(f"so you: {report.grade()}")
       
class EmailReport:
    def emailreport(self):
        print("we are sent your grade thruogh the link ,please check through the below\n")

data=BuildReport("roba","ets1099/13")
email=EmailReport()
email.emailreport()
data.subject("bio",89)
data.subject("english",75)
data.subject("math",80)
print(data.average())
save=SavesReport()
save.savereport(data)
data.grade()

Q2
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
class Square(Shape):
    def __init__(self,size):
        self.size=size
        
    def area(self):
        return self.size*self.size

class Triangle(Shape):
    def __init__(self,height,base):
        self.height=height
        self.base=base
    def area(self):
        return self.height*self.base/2
rectangle=Rectangle(5,4)
square=Square(5)
triangle=Triangle(5,4)
shapes=[rectangle,square,triangle]
for shape in shapes:
    print(shape.area())

#Q3
class Appsetting:
    currency="ETB"
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("now i am creating AppSetting object")
            cls._instance = super().__new__(cls)
        return cls._instance
    def account(self,balance):
        print(f"{balance}{self.currency}")        
    def loan(self,balance):
        self.balance=balance
        print(f"{balance}{self.currency}")   
# Appsetting.currency="usd"
data=Appsetting()
data2=Appsetting()
data.account(90)
data2.account(78)
data2.account(7)
data2.loan(40)
print(Appsetting() is Appsetting())

#Q4
class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
class Square:
    def __init__(self,side):
        self.side=side
       
    def area(self):
        return self.side*self.side

class Triangle:
    def __init__(self,height,width):
        self.height=height
        self.base=base
    def area(self):
        return self.height*self.base/2

class AreaFactory:
    @staticmethod
    def create(kind,height,width):
        if kind == "rectangle":
            return Rectangle(height,width)
        if kind == "square":
            return Square(height)
        if kind == "triangle":
            return Triangle(height,width)

shape=AreaFactory.create("square",50,8)
print(shape.area())
#Q5
class Newsagency:
    def __init__(self):
        self.observers=[]
    def publisher(self):
        messages=f"this our day06 practice exercise and the practice of this day and now after we finished this project we gonna learn something new"
        self.notify(messages)
    def subscribe(self,obs):
        self.observers.append(obs)
    def notify(self,event):
        for obs in self.observers:
            obs.update(event)
            
class SMSAlert:
    def update(self,event):
        print(f"[Newsagency announce through your smsalert]:{event}")
class Emailalert:
    def update(self,event):
        print(f"[Newsagency announce through your emailalert]:{event}")

email=Emailalert()
sms=SMSAlert()
agency=Newsagency()

agency.subscribe(email)
agency.subscribe(sms)

agency.publisher()
