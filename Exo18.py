
numbers = [1, 2, 3, 4, 5]

while True:
   
    print("\nMenu :")
    print("1. Ajouter un élément")
    print("2. Insérer un élément à une position spécifique")
    print("3. Supprimer un élément (pop)")
    print("4. Supprimer un élément par valeur (remove)")
    print("5. Quitter")
    
   
    choice = input("Choisissez une option (1-5) : ")
    
    if choice == "1":
        value = int(input("Entrez l'élément à ajouter : "))
        numbers.append(value)
    elif choice == "2":
        value = int(input("Entrez l'élément à insérer : "))
        position = int(input("Entrez la position où insérer l'élément : "))
        numbers.insert(position, value)
    elif choice == "3":
        index = int(input("Entrez l'index de l'élément à supprimer (pop) : "))
        if 0 <= index < len(numbers):
            numbers.pop(index)
        else:
            print("Index invalide.")
    elif choice == "4":
        value = int(input("Entrez l'élément à supprimer (remove) : "))
        if value in numbers:
            numbers.remove(value)
        else:
            print("L'élément n'est pas dans la liste.")
    elif choice == "5":
        print("Quitter le programme.")
        break
    else:
        print("Choix invalide.")
    
  
    print("Liste mise à jour :", numbers)
