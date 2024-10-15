p = input("Sir, \n\t Please input your name here :")
q = int(input("Please input your age :"))

print(f"As you entered your name {p} and age {q}") # here f allow to get the value of p and q  inside  the string , here you can also wrie as string.format(" ")
print("Thank you for giving your details. \n Have a nice day...")


l = ["Vinay", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):  # It will only pass the value to name which is starting from S
        print(f"Hello {name}")
        
print("Thank you")