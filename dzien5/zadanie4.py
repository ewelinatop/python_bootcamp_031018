lista = []
podzielneprzez3 = []
podzielneprzez5 = []

for x in range(100):
#    if x%3 == 0:
#        podzielneprzez3.append(x)

#    elif x%5 == 0:
 #       podzielneprzez5.append(x)


    if x %3 == 0 or x %5 == 0:
        print(x)
        x +=1

print(f"W przedziale liczb 0-100 jest {x} podzielnych liczb przez 3 lub 5")

