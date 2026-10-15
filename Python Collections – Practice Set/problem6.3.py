# 3- Write a program that merges two dictionaries into one.

dict_1 = {"Rohan": 85, "Aditi": 79, "Mohit": 91}
dict_2 = {"Anjali": 65, "Abhishek": 81}

# dict_1.update(dict_2) # Use of .update, but it will change the original dict_1.
# print(dict_1)

# OR

merged_1 = {**dict_1, **dict_2}
print(merged_1)

# Or

merged_2 = dict_1 | dict_2
print(merged_2)

# OR

def merged_dict(dict_a, dict_b):
    return {**dict_a, **dict_b}
    # OR: return dict_a | dict_b

dict_a = {"Harry": 85, "Ajay": 79}
dict_b = {"Garry": 65, "Larry": 91}

print(merged_dict(dict_a, dict_b))