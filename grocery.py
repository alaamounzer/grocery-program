groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}
shop = []
while True:
    item = input("What do you want to buy? ")
    if item == "done":
        break
    elif item in groceries:
        shop.append(item)
    elif item not in groceries:
        print("Sorry, we don’t have that item.")
print ("you bought " + str(shop))
total = 0
for item in shop:
    total += groceries[item]

print("Total = " + str(total)+ "$")

if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")
