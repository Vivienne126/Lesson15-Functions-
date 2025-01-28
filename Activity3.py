def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
print("Enter you choice \n a:Add \n b.subtract \n c. multiply \n d.divide")
choice=(input("Enter your choice"))
num_1=int(input("Enter number 1"))
num_2=int(input("Enter number 2"))
if choice=="a":
    print(add(num_1,num_2))
elif choice=="b":
    print(subtract(num_1,num_2))
elif choice=="c":
    print(multiply(num_1,num_2))
elif choice=="d":
    print(divide(num_1,num_2))
else:
    print("Invalid input , please enter correct input")

