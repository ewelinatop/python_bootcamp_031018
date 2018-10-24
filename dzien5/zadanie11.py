#zbiory

"""zbior_a = {1,2,3,4,5,6}

zbior_a.add(546)

print(zbior_a)

print(type(zbior_a))

lista = [1,1,1,2,3,4,5,6,6,6]
print(set(lista))

a = {1,2,3,4}
b = {4,5,6,7}

print(a|b)
print(a-b)
print(a&b)
print(a^b)

print(list(range(1,100,2)))

print(set(range(1,100,2)))

x ={49,81, 50, 20}
y = set(range(1,100, 2))
print(x&y)"""

napis = input("Wprowadź liczby: ")

zbior = {}

for i in napis:
    if i != 0:
        zbior[i] = zbior[i].get(i,0) + 1
