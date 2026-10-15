# 2- Given a dictionary of products and their prices, find the product with the highest price.

dict1 = {"pen": 25, "pencil": 15, "scale": 10, "Sharpner": 13}
# print(max(dict1.values()))   Gives the highest value.
print(max(dict1, key = dict1.get))

# OR

def most_expensive_product(products):
    return max(products, key = products.get)

products = {
    "Laptop": 50000,
    "PC": 90000,
    "mouse": 800,
    "Monitor": 5000
}

print(most_expensive_product(products))