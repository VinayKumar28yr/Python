
#***
#* *       for n = 3
#***



n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="") # here end define that  this line is ended here and next work start with new line
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")