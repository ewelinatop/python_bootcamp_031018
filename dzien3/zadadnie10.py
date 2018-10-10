a = int(input("Podaj pierwszą liczbę "))
b = int(input("Podaj drugą liczbę "))
c = input("Podaj rodzaj operacji ")

if c == "+":
    wynik = a+b
elif c == "-":
    wynik = a-b
elif c == "*":
    wynik = a*b
elif c == "/":
    if b == 0:
        print("Nie dzielimy przez 0")
    else:
        wynik = a/b



print(f"Wynik działania {c} na argumentach {a} i {b} to {wynik}")






