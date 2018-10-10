szerokosc = int(input("Podaj wysokość"))
wysokosc = int(input("Podaj wysokość"))
dl = int(input("Podaj dl"))

objetosc = szerokosc*wysokosc*dl

if objetosc > 1000:
    print(f"Objętość większa od 1")
else:
    print(f"Objętość mnejsza od 1")