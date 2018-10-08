# To jest komentarz

""" Utwórz zmienną a i b, przypisz im wartości liczbowe

Utwórz zmienną pole prostokąta i przypisz do niej formułę liczącą te pole

wypisz na wyjście standardowe teskt: pole prostokąta o bokach: 1,2 wynosi 4

ctrl+alt+L
ctrl+shift+f10

wypisz też tekst  dokładnie jak poniżej

"To jest tekst w cudzysłowie"

ctrl /


"""

a = 2
b = 2
pole_prostokata = a*b
print("pole prostokąta o bokach: "+ str(a)+" i "+ str(b)+" wynosi "+str(pole_prostokata))
print(f"pole prostokąta o bokach: {a}, {b} wynosi {pole_prostokata}")
# print('"To jest tekst w cudzysłowie"')
# print("\"To jest tekst w cudzysłowie\"")
# print("To jest\nwieloliniowy\ntekst")

a = int(input("Podaj bok a"))
b = int(input("Podaj bok b"))
pole_prostokata = a*b
print(f"pole prostokąta o bokach: {a}, {b} wynosi {pole_prostokata}")

a = int(input("Wzrost"))
b = int(input("Wiek"))
print(f"{a}")
        
