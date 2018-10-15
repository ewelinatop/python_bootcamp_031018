from random import randint

graczX = randint(1,10)
graczY = randint(1,10)

skarbX = randint(1,10)
skarbY = randint(1,10)

minKrokowPrzed =abs(skarbX - graczX) + abs(skarbY - graczY)

while True:
    wejscie = input("Podaj kierunek: ")

    print(f"Jestes na wspolrzednych ({graczX}, {graczY})")

    if wejscie == "w":
        graczY += 1
    elif wejscie == "s":
        graczY -= 1
    elif wejscie == "a":
        graczX -= 1
    elif wejscie == "d":
        graczX += 1


    if graczX == skarbX and graczY == skarbY:
        print("znalazłeś skarb")
        break
    """ if minKrowkowPO == 0:
        print("Znalazles skarb")"""

    minKrokowPo = abs(skarbX - graczX) + abs(skarbY - graczY)

    if minKrokowPrzed < minKrokowPo:
        print("oddalasz się")
    else:
        print("Zbliżasz się")

    if graczX >10 or graczX<1 or graczY >10 or graczY <1:
        print("jesteś poza planszą")
        break

    print(f"Znalazłeś skarb po : {abs(minKrokowPo-minKrokowPrzed)} krokach")

