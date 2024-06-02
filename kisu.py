string = "Chicken_Cheeseburger-2, Fries-3, Soft_Drinks-3"

x = string.replace("_", " ").replace("-", ",").split(",")
for i in range(0, len(x), 2):  # Start from 0 and skip every other element
    x[i] = int(x[i])  # Convert the element to an integer

print(x)
