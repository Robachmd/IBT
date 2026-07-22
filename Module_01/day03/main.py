
from io import UnsupportedOperation
customer={
    
}

try:
    with open("transactions.txt") as tr:
        
        for line in tr:
            name,amount=line.strip().split(",")
            amount = int(amount)
            if name in customer:
                customer[name]+=amount
            else:
                customer[name]=amount
        
except UnsupportedOperation:
    print("UnsupportedOperation")
except FileNotFoundError:
    print("No such file or directory")
except ValueError:
    print("not enough values to unpack")
else:
    def get_list(x):
        return int(x[1])
    
    with open("report.txt","w") as f:
        f.write("This file is the summary of sorted_customer form from the highest to lowest expense\n")
        value_list = list(customer.items())
        value_list.sort(key=get_list , reverse=True)
        
        for name,amount in value_list:
          
            f.write(f"{name},{amount}\n")
print(value_list)

print(customer)

