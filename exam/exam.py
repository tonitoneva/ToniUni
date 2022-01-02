number_of_cities = int(input())
city_list = []
incomes = []
expenses_list = []

counterOfCities = 1

total_profit = 0

for city in range(0, number_of_cities):
    name_of_the_city = input()
    income = float(input())
    expenses = float(input())
    city_list.append(name_of_the_city)
    incomes.append(float(income))
    expenses_list.append(float(expenses))

for city in range(0, number_of_cities):
    incomePerCity = incomes[city]
    expensesPerCity = expenses_list[city]
    if counterOfCities % 3 == 0 and counterOfCities != 15:
        expensesPerCity = expensesPerCity + expensesPerCity/2
    if counterOfCities % 5 == 0:
        expensesPerCity += incomePerCity/10
    profit = incomePerCity - expensesPerCity
    total_profit += profit
    counterOfCities += 1
    print(f"In {city_list[city]} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")