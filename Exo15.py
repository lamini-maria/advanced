mot = input("Please type in a string: ")
A = False
O = False
E = False
for i in range(len(mot)) :
    if mot[i] == "a" :
        A = True
    if mot[i] == "o" :
        O = True
    if mot[i] == "e" :
        E = True
if A == True :
    print("a found")
else:
    print("a not found")
if E == True :
    print("e found")
else:
    print("e not found")
if O == True :
    print("o found")
else:
    print("o not found")
