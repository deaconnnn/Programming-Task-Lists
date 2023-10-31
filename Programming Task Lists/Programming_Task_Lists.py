print("\nWelcome! What would you like?")
print("\nPizza sold at £7.30 \nPie sold at £3.45 \nBurger sold at £4.50 \nChips sold at £2.00 \nOnion rings ordered at £2.30 \nA drink at £1.50")

order = []
total = 0
Pizza = 7.30
Pie = 3.45
Burger = 4.50
Chips = 2.00
Onion_rings = 2.30
drink = 1.50


order_input = input("\nWhat would you like to order?: ")
if order_input == "pizza":
        total += 7.30
        order.append("pizza 7.30")
elif order_input == "pie":
        total += 3.45
        order.append("pie 3.45")
elif order_input == "burger":
        total += 4.50
        order.append("burger 4.50")
elif order_input == "chips":
        total += 2.00
        order.append("chips 2.00")
elif order_input == "onion rings":
        total += 2.30
        order.append("onion rings 2.30")
elif order_input == "drink":
        total += 1.50
        order.append("drink 1.50")
else:
    print("\nThats not on the menu please try again!")
   
running = True
while running == True:   
    order_input2 = input("\nWould you like anything else? (Say 'n' if no): ")
    if order_input2 == "pizza":
        total += 7.30
        order.append("pizza 7.30")
    elif order_input2 == "pie":
        total += 3.45
        order.append("pie 3.45")
    elif order_input2 == "burger":
        total += 4.50
        order.append("burger 4.50")
    elif order_input2 == "chips":
        total += 2.00
        order.append("chips 2.00")
    elif order_input2 == "onion rings":
        total += 2.30
        order.append("onion rings 2.30")
    elif order_input2 == "drink":
        total += 1.50
        order.append("drink 1.50")
    
    elif order_input2 == "n":
        print(f"\nThankyou for ordering your total is: {total}")
        print(f"\nYour reciept is: {order}")
        running = False

    else:
        print("\nThats not on the menu please try again!")
  


