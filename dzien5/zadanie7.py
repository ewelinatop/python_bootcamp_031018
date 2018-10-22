#napis = "Ala ma kota".lower()
#print(napis[0])

#print("m" in napis)

#for litera in napis:
#    print(litera.upper())

napis = input("Wprowadź tekst: ")

print(napis)

samogloski = "aeiouy"

licznik = 0

for litera in napis:
    if litera in samogloski:
        licznik +=1
print(f"W napisie jest {licznik} samoglosek")
