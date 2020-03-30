from math import sqrt, ceil

def czy_pierwsza(a):
    if a<2:
        return False
    if a%2==0 and a!=2:
        return False
    for x in range(3, ceil(sqrt(a))+1, 2):
        if a%x==0:
            return False
    return True

def bin_dec(a):
    potega, suma=1, 0
    while a>0:
        suma+=a%10*potega
        a//=10
        potega*=2
    return suma

def dow_dec(a, b):
    potega=1
    suma= 0
    a=int(a)
    if a<0:
        a*=-1
        while a>0:
            suma+=((a%10)*potega)
            a//=10
            potega*=b
        return -suma
    else:
        while a > 0:
            suma += ((a % 10) * potega)
            a //= 10
            potega *= b
        return suma

def strdow_dec(a,b):
    suma=int()
    potega=1
    for x in range(len(a)-1,-1,-1 ):
        suma+=int(a[x])*potega
        potega*=b
    return suma

def dec_bin(a):
    suma = str()
    jed=1
    if a < 0:
        a *= -1
        jed=-1
    while a > 0:
        suma = chr(a % 2 + 48) +suma
        a = a // 2

    return int(suma)*jed

def zadanie1():
    dane = list()
    with open('dane_systemy1.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane.append(lines)
            lines = plik1.readline().split()
    min = 1000
    for a in dane:
        temp = dow_dec(int(a[1]), 2)
        if temp < min:
            min = temp
    with open("wyniki58.txt", 'a') as odp:
        odp.write(f'{dec_bin(min)}\n')
    #print(dec_bin(min))

    # dane=list()
    with open('dane_systemy2.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane.append(lines)
            lines = plik1.readline().split()
    min = 1000
    for a in dane:
        temp = dow_dec(int(a[1]), 4)
        if temp < min:
            min = temp
    with open("wyniki58.txt", 'a') as odp:
        odp.write(f'{dec_bin(min)}\n')
    #print(dec_bin(min))

    dane = list()
    with open('dane_systemy3.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane.append(lines)
            lines = plik1.readline().split()
    min = 1000
    for a in dane:
        temp = dow_dec(int(a[1]), 8)
        if temp < min:
            min = temp
    with open("wyniki58.txt", 'a') as odp:
        odp.write(f'{dec_bin(min)}\n')
    #print(dec_bin(min))

def zadanie2():
    dane = list()
    dane2 = list()
    dane3 = list()
    with open('dane_systemy1.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane.append(lines)
            lines = plik1.readline().split()
    with open('dane_systemy2.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane2.append(lines)
            lines = plik1.readline().split()
    with open('dane_systemy3.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane3.append(lines)
            lines = plik1.readline().split()
    a = strdow_dec(dane[0][0], 2)
    b = strdow_dec(dane2[0][0], 4)
    c = strdow_dec(dane3[0][0], 8)
    licznik = 0
    for x in range(1, 1095):
        if strdow_dec(dane[x][0], 2) % 12 != 0 and strdow_dec(dane2[x][0], 4) % 12 != 0 and strdow_dec(dane3[x][0],
                                                                                                       8) % 12 != 0:
            licznik += 1
    with open("wyniki58.txt", 'a') as odp:
        odp.write(f'{licznik}\n')
    #print(licznik)

def zadanie3():
    dane = list()
    dane2 = list()
    dane3 = list()
    with open('dane_systemy1.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane.append(lines)
            lines = plik1.readline().split()
    with open('dane_systemy2.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane2.append(lines)
            lines = plik1.readline().split()
    with open('dane_systemy3.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane3.append(lines)
            lines = plik1.readline().split()

    max1 = dow_dec(int(dane[0][1]), 2)
    max2 = dow_dec(int(dane2[0][1]), 4)
    max3 = dow_dec(int(dane3[0][1]), 8)
    dni = 1
    for x in range(1, 1095):
        if dow_dec(int(dane[x][1]), 2) > max1 or dow_dec(int(dane2[x][1]), 4) > max2 or dow_dec(int(dane3[x][1]),
                                                                                                8) > max3:
            dni += 1
            if dow_dec(int(dane[x][1]), 2) > max1:
                max1 = dow_dec(int(dane[x][1]), 2)

            if dow_dec(int(dane2[x][1]), 4) > max2:
                max2 = dow_dec(int(dane2[x][1]), 4)

            if dow_dec(int(dane3[x][1]), 8) > max3:
                max3 = dow_dec(int(dane3[x][1]), 8)
    with open("wyniki58.txt", 'a') as odp:
        odp.write(f'{dni}\n')
    #print(dni)

def zadanie4():
    dane = list()
    with open('dane_systemy1.txt', 'r') as plik1:
        lines = plik1.readline().split()
        while len(lines) > 0:
            dane.append(lines)
            lines = plik1.readline().split()
    maks = 0
    for x in range(1095):
        for y in range(x + 1, 1095):
            roznica = (dow_dec(dane[x][1], 2) - dow_dec(dane[y][1], 2)) ** 2
            bez = abs(x - y)
            skok = ceil(roznica / bez)
            if skok > maks:
                maks = skok
    with open("wyniki58.txt", 'a') as odp:
        odp.write(f'{maks}\n')


zadanie1()
zadanie2()
zadanie3()
zadanie4()
print(bin_dec(-1010101))


