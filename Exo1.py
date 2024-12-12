# Ask the user for their name
name = input("Please enter your name: ")

if name == "VIP":
    print("Enjoy the show for free!")
else:
    # Ask how many tickets the user wants to buy
    try:
        tickets = int(input("How many tickets would you like to buy? "))
        ticket_price = 15.50
        total_cost = tickets * ticket_price
        print(f"The total cost is {total_cost}")
        print("Enjoy your tickets!")
    except ValueError:
        print("Invalid input. Please enter a valid number of tickets.")
