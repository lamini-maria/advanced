words = [] 
while True:
    word = input("Entrez un mot : ")
    
   
    if word in words:
        print("Vous avez tapé 2 mots identiques.")
        break
    else:
        words.append(word)

