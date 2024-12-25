while True : 
    value = int(input("Veuillez saisir un nombre entier positif :"))
    if value > 0 :
        for i in range(-value, value + 1) : 
           if i != 0 :
               print(i)
    else :
        print("Le nombre doit être positif. Essayez encore.")
    