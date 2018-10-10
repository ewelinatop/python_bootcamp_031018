x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if (x > 100 and y > 100) or (x<0 and y<0):
    pozycja = "poza planszą"

elif (x <10 and y <10):
    pozycja = "Zmajdujesz się w LD rogu"
elif (x >10 and x <90 and y<10):
    pozycja = "Zmajdujesz się w DK"
elif (x > 90 and y < 10):
    pozycja = "Zmajdujesz się w PD"
elif (x > 90 and y > 10 and y < 90):
    pozycja = "Zmajdujesz się w PK"
elif (x > 90 and x < 100 and y > 90 and y <100):
    pozycja = "Zmajdujesz się w PG"
elif (x >10 and x <90 and y >90 and y <100):
    pozycja = "Zmajdujesz się w GR"

else:
    pozycja = "centrum"

print (f"Twoja pozyjca to: {pozycja}")