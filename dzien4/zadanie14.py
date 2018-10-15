znalezione_max = None
znalezione_min = None

while True:
    wejscie = input("Podaj liczbę: ")

    if (wejscie == "koniec"):
        break

    x = int(wejscie)

    if znalezione_max is None or x > znalezione_max:
        znalezione_max =x

    if znalezione_min is None or x < znalezione_min:
        znalezione_min = x

if znalezione_max is None:
    print("Nie wprowadzaj danych, wyliczyliśmy już wynik")
else:
    print(f"max: {znalezione_max} min:{znalezione_min}")




