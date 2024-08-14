def main():
    while True:
        amt_due = 50
        print(f"Amount Due: {amt_due}")

        while amt_due > 0:
            coin = int(input("Insert Coin: "))

            if coin not in [5, 10, 25]:
                break

            amt_due -= coin
            if amt_due <= 0:
                break

            print(f"Amount Due: {amt_due}")

        if amt_due <= 0:
            change = -amt_due
            print(f"Change Owed: {change}")
            break

main()
