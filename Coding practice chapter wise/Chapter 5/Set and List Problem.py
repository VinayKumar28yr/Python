#s = {8, 7, 12, "Vinay", [1,2]}

# s[4][0] = 9   It will show error because SET is immutable
# print(s) 


s = [(8,), (7,), (12,), ("Vinay",), [1, 2]] # This is list

# Now you can modify the list
s[4][0] = 9

print(s)  # Outputs: [(8,), (7), (12), ('Harry',), [9, 2]]
