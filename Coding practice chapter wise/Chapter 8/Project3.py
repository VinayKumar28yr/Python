def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)



a = int(input("Enter the number : "))
print(pattern(a))
