def zad1():
    with open("ciagi.txt", 'r') as plik:
        licznik = 0
        for line in plik:
            liczba = line.strip()
            if len(liczba) % 2 == 0:
                prawda = False
                if liczba[0:len(liczba) // 2] == liczba[len(liczba) // 2:len(liczba)]:
                    licznik += 1
                    print(liczba)
                    prawda = True
                '''prawda = True
                for x in range(0, len(liczba)//2):
                    if liczba[x]!=liczba[x+len(liczba)//2]:
                        prawda = False
                        break
                if prawda == True:
                    print(liczba)
                    licznik+=1'''
        #print(licznik)

def zad2():
    with open("ciagi.txt", 'r') as plik:
        licznik = 0
        for line in plik:
            liczba = line.strip()
            prawda = True
            for x in range(len(liczba) - 1):
                if liczba[x] == '1':
                    if liczba[x + 1] == '1':
                        prawda = False
                        break
            if prawda == True:
                licznik += 1
    print(licznik)

def czy_polpierwsza(a):
    dzielnik = 2
    licznik = 0
    while a>1:
        if a%dzielnik==0:
            a/=dzielnik
            licznik+=1
        else:
            dzielnik+=1
    if licznik == 2 :
        return True
    return False

def zad3():
    with open("ciagi.txt", 'r') as plik:
        licznik = 0
        maks = 0
        mini = 1000
        for line in plik:
            liczba1 = line.strip()
            liczba = int(liczba1, 2)
            if czy_polpierwsza(liczba) == True:
                licznik += 1
                if liczba > maks:
                    maks = liczba
                if liczba < mini:
                    mini = liczba
        print("maks ", maks)
        print("mini ", mini)
        print("ilosc liczb ", licznik)






#zad1()

#zad2()

#zad3()

