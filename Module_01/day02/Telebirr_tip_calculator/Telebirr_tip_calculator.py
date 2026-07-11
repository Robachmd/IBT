#Telebirr tip calculator project
total=4500
people=5
names=['roba','kebede','chala','sami','bruk']

def split_bill(total,people,tip_rate=0.10):
    total_price = total*tip_rate + total
    result= (total*tip_rate + total)/people
    print(f"Hello friends our total bill is {total_price}")

    for name in names:
        print(f"hello {name} your share is {result}")
split_bill(total,people)