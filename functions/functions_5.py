

def calculate_total_price(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.5
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2.0

    total_price = price * quantity
    return total_price
product_name = input()
product_quantity = int(input())
res = calculate_total_price(product_name, product_quantity)
print(f"{res:.2f}")
