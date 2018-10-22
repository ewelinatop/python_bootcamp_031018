produkty = {"ziemniaki": 5, "marchew": 9, "pomidory": 7}

print("w naszym sklepie oferujemy :")

for produkt in produkty:
    print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

print()

wybor_produktu = input("Który produkt chcesz kupić? ")

ile = input(f"Ile chcesz kupić [{wybor_produktu}]")

cena = float(ile)*produkty[wybor_produktu]

print(f"Zaplacisz: {cena}")







