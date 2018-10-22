liczby = [5, 2, 3, 1, 4]
#indeksy = [0,1,2,3,4]

#min_ = None
#max_ = None


min_ = liczby[0]
max_ = liczby[0]


for liczba in liczby:
    if liczba < min_:
        min_ = liczba
    if liczba > max_:
        max_ = liczba

 liczby[liczby.index(min_)], liczby[liczby.index(max_)] = max_, min_


print(min_, max_)
print(liczby.index(min_), liczby.index(max_))


liczby[liczby.index(min_)]= max_
liczby[liczby.index(max_)]= min_


#for i in range(len(liczby)):
#    print(liczby[i])

assert liczby == [1,2,3,4,5]



#liczby = [1,2,3]
#x = liczby[0] #x=1
#liczby[0] = liczby[2] # [3,2,3]
#liczby[2] = x #[3,2,1]
