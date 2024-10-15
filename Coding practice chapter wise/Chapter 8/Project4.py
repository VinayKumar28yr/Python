def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.replace(word, ""))
    return n


l = ["Vinay", "Rohan", "Shubham", "an"]

print(rem(l, "an"))
