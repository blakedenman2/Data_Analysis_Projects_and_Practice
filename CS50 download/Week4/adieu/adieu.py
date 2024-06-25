import inflect
p = inflect.engine()

names = []

while True:
    try:
        words = input("Name: ")
        names.append(words)
    except EOFError:
        break

peeps = p.join(names)
print(f"Adieu, adieu, to {peeps}")

