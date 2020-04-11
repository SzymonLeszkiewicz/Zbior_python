with open("ciagi.txt", 'r') as plik:
    ile = int(plik.readline().strip())
    while ile> 0 :
        for x in range(ile):
            liczba=plik.readline()
            print(liczba)
        ile = plik.readlines()