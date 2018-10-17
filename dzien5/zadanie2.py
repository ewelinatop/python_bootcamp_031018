pusta_tupla = ()

jeden_element = (4,)

# lista

lista = []

while len(lista) < 10:
    x = input("Podaj liczbę:  lub 'k' żeby zakończyć")
    if x == "k":
        break

    liczba = int(x)
    lista.append(liczba)

srednia = sum(lista)/ len(lista)

if len(lista) == 0:
    print("nie podano danych")
else:
    srednia = sum(lista) / len(lista)
    print(f"Srednia to {srednia}")

print(f"Srednia to {srednia}")





