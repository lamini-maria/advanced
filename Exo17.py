numbers = []
shoe_sizes = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)
print("Liste des numéros :", numbers)
print("Liste des tailles de chaussures :", shoe_sizes)
numbers.append(3)  # Ajout d'un doublon
numbers.append(1)  # Ajout d'un doublon
numbers = list(set(numbers))
combined_list = numbers + shoe_sizes
print("Liste des numéros sans doublons :", numbers)
print("Liste combinée :", combined_list)