menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    price = 0.0
    while True:
        try:
            order = (input("Item: ").title())
            test = check(order)
            if test == False:
                pass
            else:
                cost = check(order)
                price += float(cost)
                print(f"Total: ${price:.2f}")

        except EOFError:
            print("\n", end = "")
            break

def check(item):
    price = menu.get(item, False)
    return price

main()
