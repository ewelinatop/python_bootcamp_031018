napis = input("wprowadź tekst :")

licznik = {}

for l in napis:
    if l != " ":
        licznik[l] = licznik.get(l,0) + 1

#    if l in licznik:
#       licznik[l] = licznik[l] + 1
#    else:
#        licznik[l] = 1

print(licznik)


#input("cos").lower()


