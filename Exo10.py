mot = input("Entrer le mot :")
pal = True
for i in range(len(mot)) :
    if mot[i] != mot[-(i + 1)] :
      pal = False
if pal == True :
   print("Yes, it's a palindrome.")
else :
   print("No, it's not a palindrome.")