item = input("What item would you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many items would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")