# String methods and functions

# Note: Strings are immutable, means you can change the strings using functions and methods but you cannot change the actual string in the memory, making it immutable.

# Examples: common string methods

# Changing Case:

text = "hello world"

print(text.upper())   # All the characters are uppercase
print(text.lower())   # All the characters are lowercase
print(text.capitalize())   # Only the first character of the first word is uppercase/or capital
print(text.title())   # Every word's first character is uppercase/or capital


# Removing Whitespace:

sentence = "\n  hello python!  \n"

print(sentence.strip())   # Remove the extra whitespaces and newlines from both sides
print(sentence.lstrip())   # Remove the extra whitespaces and newlines from left sides only
print(sentence.rstrip())   # Remove the extra whitespaces and newlines from right sides only


# Finding and Replacing:

word = "My name is Mohit"

print(word.find("is"))   # It will tell you the index of the particular string, but only the first occuring character, i = 8 it will not count or print s = 9.
print(word.replace("Mohit", "mohit"))   # It replaces the word and it will replace all the occurances, if there are multiple words.


# Splitting and Joining

g = "It will split the sentence"   # Split method divides the string into parts(substrings) based on a seperator, by default it splits whenever there's a space, it returns a list of strings.
result = (g.split())   # You can specify a seperator as well.
print(result)

h = ['It', 'will', 'join', 'the', 'sentences']   # Joining does the opposite of split, it combines a list of string into one, using a seperator you choose.
results = "-".join(h)   # With hyphen
print(results)


# Checking String Properties: it gives the output in true or false.

x = "Mohit123"

print(x.isalpha())   # Are all the characters, alphabet or not
print(x.isdigit())   # It will tell whether its digit or not, when its a digit ? when it can be converted into an integer.
print(x.isalnum())   # Tell if a string is alphanumeric or not
print(x.isspace())   # True if all the characters are whitespace


# Examples: string functions

z = "Functions of strings"
y = len(z)   # len (lenght) it tells you the lenght of the strings, here its = 20 
print(y)

print(ord('A'))   # ord 
print(chr(34))   # And chr are used for character encoding, its gives you the ascii value and if you tell the value it will give you the character in return.