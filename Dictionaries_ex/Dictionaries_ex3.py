list_of_countries = input().split(", ")
list_of_capitals = input().split(", ")
dictionary_of_countries_capitals = {}
counter = 0

for countries in list_of_countries:
    dictionary_of_countries_capitals[countries] = list_of_capitals[counter]
    counter += 1

for country, capital in dictionary_of_countries_capitals.items():
    print(f"{country} -> {capital}")

