price = float(input("Please type in a price: "))
dinars = int(price)
centimes = int(round((price - dinars) * 100))


print(f"Dinars: {dinars}")
print(f"Centimes: {centimes:02d}")