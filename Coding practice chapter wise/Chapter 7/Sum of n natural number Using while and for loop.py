n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1

print(sum)

# Using for loop
n = int(input("Enter the number: "))
sum = 0

for i in range(1, n+1):
    sum += i

print(sum)

# For factorial using for loop
n = int(input("Enter the number: "))
factorial = 1

for i in range(1, n+1):
    factorial = factorial*i

print(factorial)

# For factorial using while loop
n = int(input("Enter the number: "))
i = 1
factorial = 1
while(i<=n):
    factorial = factorial*i
    i+=1

print(factorial)


