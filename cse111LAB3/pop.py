x = "Chicken_Cheeseburger-2, Fries-3, Soft_Drinks-3"

items = x.replace("_", " ").replace("-", ",").split(",")
for i in range(1, len(items), 2):
    items[i] = int(items[i])


print(items)
