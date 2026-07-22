#q1
weather= int(input("what is the weather temprature now?"))
if weather > 28:
    print("it is hot")
elif weather <= 28 and weather >= 15:
    print("it is average")
else:
    print("cold")
#q2
for i in range (1,11):
    print("receipt #",i)
#q3
for i in range (21):
    if i%2 == 0:
        print(i)
#q4
def apply_discount(price,percent = 10):
    result= price - (percent/price)*100
    return result
print(apply_discount(23456))
#q5
i = 5
while i >= 1:
    print(i)
    i-=1
    
 #q6   
current_year = 2026
birth_year = 2001
age = current_year - birth_year

print(f"You are {age} years old.")