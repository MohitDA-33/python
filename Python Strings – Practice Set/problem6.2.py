# Take a user input string and check if it is a palindrome (same forwards and backwards).

string1 = input("Enter a string: ")

if (string1 == string1[::-1]):
    print("This string is a palindrome")

else:
    print("This string is not a palindrome")

# Palindrome is a sequence of characters that reads the same forward and backward
# Examples of palindrome = level. madam, 45554