def zad1():
    with open("liczby.txt", "r") as plik:
        liczba = plik.readline().strip()
        osta = 0
        przed = 0
        licznik = 0
        while len(liczba) > 0:
            if int(liczba) < 1000:
                licznik += 1
                przed = osta
                osta = (int(liczba))
            liczba = plik.readline().strip()
        print(przed)
        print(osta)
        print(licznik)

def iled(a):
    i=1
    lista = list()
    dziel=0
    while i<=a:
        if a%i==0:
            dziel+=1
            lista.append(i)
        i+=1
    if dziel == 18:
        print(a)
        print(lista)
    return 0

def zad2():
    with open("liczby.txt", "r") as plik:
        licznik = 0
        for line in plik:
            liczba = int(plik.readline().strip())
            iled(liczba)

#zad1()
#zad2()

def nwd(a, b):
    while a:
        a=a%b
        b=b-a
    return b

with open("liczby.txt", "r") as plik:
    maks=0
    tablica=list()
    for line in plik:
        liczba = line.strip()
        with open("wyniki.txt", 'a') as wyniki:
            wyniki.write(f'{liczba}\n')

        #tablica.append(liczba)


    '''for lina in plik:
        if line!=lina:
            liczba1=int(plik.readline().strip())
            #print(liczba1,"  ", liczba)
            if nwd(liczba, liczba1)==1:
                if liczba>maks:
                    maks=liczba'''

