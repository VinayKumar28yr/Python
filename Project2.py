def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n


a = int(input("Enter the number : "))
print(sum(a))

#uppose a = 5:

# Initial Call: sum(5)

# n != 1, so it returns sum(4) + 5.

# Recursive Call: sum(4)

# n != 1, so it returns sum(3) + 4.

# Recursive Call: sum(3)

# n != 1, so it returns sum(2) + 3.

# Recursive Call: sum(2)

# n != 1, so it returns sum(1) + 2.

# Base Case Reached: sum(1)

# n == 1, so it returns 1.