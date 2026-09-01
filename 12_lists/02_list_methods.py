# List Methods: any method that we run or use will change the actual or the original lists.

marks = [77, 51, 89, 93, 97]
extra_marks = [91, 92, 93, 94, 95]
print(marks)   # It will print the original list that we have created, very basic.


# Common list methods:
marks.copy()   # .copy will give a copy of the list, containing the same elements
print(marks)

# lets use it in a different way.
a = [1, 2, 3]
b = a.copy()
print(a)
print(b)
print(b is a)   # Conclusion: It will show false, even its a copy changing in original doesnt affect the other/copied on.

marks.append(99)   # .append this method will append 99 in the end of the list.
print(marks)

marks.sort()   # .sort it will sort the elements from lowest to the highest.
print(marks)

marks.reverse()   # .reverse will reverse the output
print(marks)

marks.pop()   # .pop will remove the last element of the list, by default its last.
print(marks)   # The last element is 51.

marks.remove(99)   # .remove will remove the element from the list that you have defined to remove.
print(marks)

marks.insert(2, 100)   # Insert the element/object 100 in the index no 2.
print(marks)

marks.extend(extra_marks)   # It will extend the list, by combining the marks and extra marks elements together and will return a final list.
print(marks)

marks.clear()   # .clear will remove all the elements
print(marks)
