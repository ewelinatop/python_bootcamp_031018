suma = 0
i = 0


while True:
    dane = input("podaj tem albo wpisz k by zakończyc")

    if dane=="k":
        break


    suma +=float(dane)
    i +=1
    print("Srednia temto ", round(suma/i,2))