cities = []
while (1):
    city = input("Type in a city:  ")
    if city.lower() == "stop":
        break
    population = len(city) * 1000000
    cities.append((city, population))
for city, population in cities:
    print(f"City: {city}, Population: {population}")
