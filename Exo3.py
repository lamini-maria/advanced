total = float(input("Total amount:"))
nbr = int(input("Number of itemes  "))
jour = input ("Day of the week  ")

if nbr > 5 :
    discount = 0.05 * total
    total -= discount
    print(f"Total price after discount: {total:.2f}" )

if jour in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    discount = 0.1 * total 
    total -= discount
    print(f"Total price after discount: {total:.2f}" )

if jour == "Saturday" or jour=="sunday" :
    discount = 0.2* total
    total -= discount
    print(f"Total price after discount: {total:.2f}")
    
