miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystnas = int(input(f"Dystans {miasto_a}-{miasto_b}"))
cena = float(input("cena paliwa: "))
spalanie = float(input("Splanie na 100 km: "))

koszt = round((dystnas / 100)* spalanie * cena, 2)

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt} PLN")