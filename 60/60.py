def zad1():
    with open("liczby.txt", "r") as plik:
        with open("wyniki.txt", 'a') as wyniki:
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
            wyniki.write("Miejszych od 100: %d" %licznik)
            wyniki.write("\n Dwie ostatnie to : %s %s" %(osta, przed))
            wyniki.write(" \n \n ")

def iled(a):
    with open("wyniki.txt", 'a') as wyniki:
        i=1
        lista = list()
        dziel=0
        while i<=a:
            if a%i==0:
                dziel+=1
                lista.append(i)
            i+=1
        if dziel == 18:
            wyniki.write("\n %s  " %a)
            wyniki.write("\n %s" %lista)
        return 0

def zad2():
    with open("liczby.txt", "r") as plik:
        with open("wyniki.txt", 'a') as wyniki:
            licznik = 0
            for line in plik:
                liczba = int(plik.readline().strip())
                iled(liczba)
            wyniki.write("\n \n ")

def nwd(a, b):
    while a:
        a=a%b
        b=b-a
    return b

def zad3():
    with open("liczby.txt", "r") as plik:
        with open("wyniki.txt", 'a') as wyniki:
            maks = 0
            tablica = list()
            for line in plik:
                liczba = int(line.strip())
                tablica.append(liczba)
            # uzupełniona tablica

            for x in tablica:
                prawda = True
                for y in tablica:
                    if x == y:
                        continue
                    if nwd(x, y) > 1:
                        prawda = False
                        break
                if prawda == True:
                    if x > maks:
                        maks = x
            wyniki.write("Najwieksza liczba to %s" % maks)

zad1()
zad2()
zad3()

