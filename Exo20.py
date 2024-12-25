nbrs = []
while True :
    value = int(input("Entrez un numéro : "))
    if value == 0 :
        break
    else : 
     nbrs.append(value)
     print("Liste actuelle :" , nbrs)
     nbrs.sort()
     print("Liste triee : " , nbrs)