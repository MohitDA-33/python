'''
2 - Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

Both length and width
Only length (use default width)
'''

def calculate_area(lenght, width=10):
    area = lenght * width
    return area

rectangle_1 = calculate_area(13)
print(rectangle_1)
rectangle_2 = calculate_area(13, 20)
print(rectangle_2)