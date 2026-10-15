'''
6. Bonus Challenges

1- Write a program that takes a list of numbers and removes all duplicates using a set.
'''

list1 = [78, 3, 33, 91, 5, 1, 3, 33]
se = set(list1)
print(se)

# OR

def remove_duplicates(list2):
    return list(set(list2))

list2 = [78, 3, 33, 91, 5, 1, 3, 33]
print("Original list:", list2)
print("Without Duplicates:", remove_duplicates(list2))