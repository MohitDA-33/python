# Dictonaries and Dictionary Methods

# Dictionary: they store the values in key-value pairs and allow fast lookups, after storing elements you can fetch them very fast.

marks = {"Mohit": 93, "Aditi": 88, "Shreya": 91}
print(marks)   # It prints the output in key-value pair.
print(type(marks))
print(marks["Mohit"])
print(marks["Aditi"])

marks["Aditi"] = 92   # You can always change the content of a dictionary, here we are updating a value(88-->92) of a key("Aditi").
print(marks)

marks["Shraddha"] = 95   # Adding a new key-valuue pair.
print(marks)

# You can add a content in a dictionary, you can update the value, add a new one, or remove all these things are doable.