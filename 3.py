month = input()
hours = int(input())
people = int(input())
day_or_night = input()

if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        price = 10.50
    elif day_or_night == "night":
        price = 8.40
elif month == "june" or month == "july" or month == "august":
    if day_or_night == "day":
        price = 12.60
    elif day_or_night == "night":
        price = 10.20

if people >= 4:
    price = price - (price * 10/100)

if hours >= 5:
    price = price - (price * 50/100)

total = (price * people) * hours
print (f"Price per person for one hour:{price: .2f}")
print (f"Total cost of the visit:{total: .2f}")
