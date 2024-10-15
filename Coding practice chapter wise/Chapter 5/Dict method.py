marks = {
    "Vinay": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Industry"
}

print(marks.items())   #the OUTPUT is "dict_items([('Vinay', 100), ('Shubham', 56), ('Rohan', 23), (0, 'Industry')])"
print(marks.keys())    # The OUTPUT is "dict_keys(['Vinay', 'Shubham', 'Rohan', 0])"
print(marks.values())
marks.update({"Vinay": 99, "Renuka": 100}) # isme "Vinay" ko update karega and "Renuka" ko add kr dega
print(marks)

print(marks.get("Vinay2")) # Prints None because it is not present in the dictonary
# print(marks["TOM2"]) # Returns an error because it is not present in the dictonary