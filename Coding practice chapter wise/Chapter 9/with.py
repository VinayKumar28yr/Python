f = open("fileRead.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("fileRead.txt") as f:
    print(f.read())

# You dont have to explicitly close the file