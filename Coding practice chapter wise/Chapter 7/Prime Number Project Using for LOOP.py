n = int(input("Enter a number: "))

for i in range(2, n): # Here range is from 2 to n-1
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")