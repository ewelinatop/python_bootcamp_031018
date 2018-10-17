"""lista = [1,2,3,"test"]

for x in lista:
    print(x)

for x in range(0,10):
    print(x)

for x in enumerate(lista, 2):
    print(x)


for idx in enumerate(lista, 2):
    print"""



#i = 0

#while i <len(lista):
#    print(lista[i])
 #   i +=1

lista = [1,2,3,5, -2, -3, -5, -8, 0]

dodatnich = 0
ujemnych = 0

for x in lista:
    if x > 0:
        dodatnich += 1

    elif x < 0:
        ujemnych += 1

        print(f"Ujemna! {dodatnich} {ujemnych}")


 # for lista in enumerate(lista):
 #     print (f"Liczba liczb dodatnich {lista}, a liczba liczb ujemnych {lista}")

