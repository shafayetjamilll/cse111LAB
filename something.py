items = ['Chicken_Cheeseburger', 2, 498, 'Fries', 3, 417, 'Soft_Drinks', 3, 150]

index = 0
total = 0
while index < len(items):
  item = items[index]
  quantity = items[index+1]
  price = items[index+2]

  print(f'{item:20} x {quantity:2} : {price:7.2f}')
  total += price
  index += 3


print('-'*35)
print(f'Total:                      {total:7.2f}')
print('-'*35)
