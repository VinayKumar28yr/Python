a = int(input("Enter your age: "))

# If statement no: 1
if(a%2 == 0):
    print("a is even")   # In this CASE "a is even or not" is skipped because  2nd if statement is running... for this see below code
# End of If statement no: 1

# If statement no: 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")  

else:
    print("You are below the age of consent")
# End of If statement no: 2

print("End of Program")

# Another method

a = int(input("Enter your age: "))

# If statement no: 1
if a % 2 == 0:
    print("a is even")
else:
    print("a is odd")

# If statement no: 2
if a >= 18:
    print("You are above the age of consent")
    print("Good for you")
elif a < 0:
    print("You are entering an invalid negative age")  
else:
    print("You are below the age of consent")

print("End of Program")

