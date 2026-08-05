# 6. Bonus Questions

# Write a program that counts how many vowels are in a given string

sentence = "Coding in Python is fun"
sum = 0
vowel = ['a', 'e', 'i', 'o', 'u']


for char in sentence.lower():
    if (char in vowel):
        sum = sum + 1

print(f"There are {sum} vowels in this sentence")