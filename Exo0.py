pertrajet = int(input("How many people need a ride?"))
pertaxi = int(input("How many people fit in one taxi?"))
 
nbr = round(pertrajet / pertaxi) 
print(f"Number of taxis needed: {nbr}")