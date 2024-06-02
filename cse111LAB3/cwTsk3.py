class Contacts:
    def __init__(self,names,numbers):
        self.names = names
        self.numbers = numbers
        self.contactDict = {}
        if len(names) != len(numbers):
         print("Contacts cannot be saved. Length Mismatch!")

        else:
            for i in range(len(names)):
             self.contactDict[names[i]] = numbers[1]
            print("Contacts saved successfully.")


names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]

m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")

names.append("Mother")
numbers.pop()

m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)

temp_m1 = m1
m1 = Contacts(names,numbers)

