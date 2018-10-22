napis="Ala ma <kota>"

nawiasy = "<>"

licznik = 0

#for i in napis:
#    if i in nawiasy:
#       licznik +=1

#        print(f"W napisie <kota> znajduje się {licznik} znaków")



czy_zliczac = False

for i in napis:
    if i == "<":
        czy_zliczac = True
    elif i == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik += 1

print(licznik)