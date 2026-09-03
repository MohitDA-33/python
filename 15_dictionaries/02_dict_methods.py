# Dictionary Methods

# Example of some common methods

age = {"Person_1": 22, "Person_2":17, "Person_3": 47, "Person_4": 49}

print(age)
print(age.keys())   # Prints only the keys that are in the dictionary, the entity at the left side. 
print(age.keys())   # Prints only the keys that are in the dictionary, the entity at the left side. 
print(age.items())   # It gives you the key and its value grouped together.
print(age.values())   # Prints only the values that are in the dictionary, the right side data. 
a = age.copy()   # Return a copy of a dictionary.
print(a)    
print(age.pop("Person_1"))   # .pop Removes the "Mohit' key and gives you the value as output.
print(age.pop("Person_2"))
print(age.clear())   # Empties the dictionary.