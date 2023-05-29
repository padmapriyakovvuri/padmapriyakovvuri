 #shopping cart program
foods =[]
prices=[]
items = 0
total = 0
while True:
  food =input("enter a food to buy( x to quit): ")
  if food.lower()=="x":
    break
  else:
    price=float( input(f" enter the price of {food}: "))
    foods.append(food)
    prices.append(price)
    items += 1

print("..... YOUR CART.....")
for i in range(items):
  print(foods[i])
  print(str(prices[i])+"€")
  total+=prices[i]
    
print("your total is:"+str(total)+"€")
