produkty = {"ziemniaki": 5, "marchew": 9, "pomidory": 7}

#slownik.get("woda", "Brak produktu")

koszyk = {}

magazyn = {

    "ziemniaki": 10,
    "marchew": 10,
    ""
}

while True:

    komenda = input("""Wybierz opcje: 
                     [d] - dodaj do magazynu
                     [k] - kup
                     [z] - zakończ""")

    if komenda == 'd':
        co = input("Jaki produkt chcesz dodać?")
        ile = int(input(f"Ile {co} chcesz dodać?"))
        magazyn[co] = magazyn.get(co, 0) + ile
        if co not in produkty:
            cena = float(input(f"Jaka cena za {co}"))
            produkty[co] = cena
    elif komenda == 'z':
        break

    print("w naszym sklepie oferujemy :")

    for produkt in produkty:
        print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

    print()

    wybor_produktu = input("Który produkt chcesz kupić? Wpisz koniec, żeby zakończyć ")

    if wybor_produktu == "koniec":
            break

    if wybor_produktu in produkty:
            ile = int(input(f"Ile chcesz kupić [{wybor_produktu}]"))

            #cena = float(ile)*produkty[wybor_produktu]

            print(f"Zaplacisz: {cena}")

            koszyk[wybor_produktu] = ile

            if ile <= magazyn[wybor_produktu]:
                koszyk[wybor_produktu] = ile
            else:
                print(f"Nie mamy tego. Pozostało: {}")

    else:
        print("Nie ma takiego produktu")

for produkt in koszyk:
    cena=koszyk[produkt]*produkty[produkt]
    print(f"Twój rachunke {produkt}: {koszyk[produkt]} PLN")
    sumarycznie += koszyk[produkt]

    print(f"Suma{sumarycznie}")











"""
produkty = {"ziemniaki": 5, "marchew": 9, "pomidory": 7}

licznik = 0

print("W sklepie są takie produkty: ")
print()

for i in produkty:
    print(i)

print()

while licznik <1 :
    towar = input("Podaj towar, który chcesz kupić: ")

    if towar in produkty:
        waga = float(input("Podaj wagę towaru: "))

        kwota = waga*produkty[towar]

        print(kwota)
        licznik +=1
        break
    else:
        print("Nie mamy takiego towaru")"""







