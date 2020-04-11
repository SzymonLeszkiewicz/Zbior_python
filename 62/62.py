def zad1():
    with open("liczby1.txt", 'r') as plik:
        maks = 0
        min = 100000
        maksliczba = str()
        minliczba = str()
        for line in plik:
            if int(line, 8) > maks:
                maks = int(line, 8)
                maksliczba = line.strip()
            if int(line, 8) < min:
                min = int(line, 8)
                minliczba = line.strip()
        print(maksliczba)
        print(minliczba)

def zad2():
    with open("liczby2.txt", 'r') as plik:
        lista = list()
        for line1 in plik:
            lista.append(int(line1.strip()))
        # koniec wczytywania int do tablicy lista
        maks = 0
        for x in range(0, len(lista)):
            licznik = 1
            pierwszy = lista[x]
            poprzednia = lista[x]
            for y in range(x + 1, len(lista)):
                if lista[y] < poprzednia:
                    if licznik > maks:
                        maks = licznik
                        najpierwszy = pierwszy
                    break
                licznik += 1
                poprzednia = lista[y]
        print(maks)
        print(najpierwszy)

def zad3():
    with open("liczby1.txt", 'r') as plik:
        lista = list()
        for line1 in plik:
            lista.append(int(line1.strip(), 8))

    with open("liczby2.txt", 'r') as plik:
        lista2 = list()
        for line2 in plik:
            lista2.append(int(line2.strip()))
    li1 = 0
    li2 = 0
    for x in range(1000):
        if lista[x] == lista2[x]:
            li1 += 1
        if lista2[x] < lista[x]:
            li2 += 1
    print(li1)
    print(li2)

def ile6(a):
    a = str(a)
    licznik = 0
    pocz = 0
    if a[0]=='0':
        pocz = 2
        #wiemy ze l jest w osemkowym
    for x in range(pocz , len(a)):
        if a[x]=='6':
            licznik+=1
    return licznik

def zad4():
    with open("liczby2.txt", 'r') as plik:
        lista = list()
        lista2 = list()
        for line in plik:
            lista.append(int(line.strip()))
            lista2.append(oct(int(line.strip())))
    licz1 = 0
    licz2 = 0
    for x in range(1000):
        licz1 += ile6(lista[x])
        licz2 += ile6(lista2[x])
    print(licz1)
    print(licz2)
#odkomentuj zadanie do którego chcesz zobaczyc odp
#zad1()
#zad2()
##zad4()