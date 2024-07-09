#Define the menu of restaurant
menu = {
    'Pizza' : 100,
    'Pasta' : 80,
    'Burger' : 70,
    'Salad' : 50,
    'Coffee' : 60,
 }

#Greet
print("Welcome to my Restaurant")
print("Pizza : Rs40\nPasta : Rs50\nBurger : Rs60\nSalad : Rs70\nCoffe : Rs80")

order_total = 0
#80 + 70 = 150

item1 = input("Enter the name of item you want to order = ")
if item1 in menu:
    order_total += menu[item1] #0 + 50
    print(f"Your item {item1} has been added to your order")

else:
    print(f"Ordered item {item1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item2 = input("Enter the name of second item = ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Item {item2} hass been added to order")
    else:
        print(f"Ordered item {item2} is not available!")

    print(f"The total amount of item to pay is {order_total}")
