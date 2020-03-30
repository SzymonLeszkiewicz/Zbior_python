def czynniki(linie):
    i = 3
    #czynniki = list()
    j = 0
    if linie % 2 == 0:
        return False
    else:
        while linie > 1:
            if linie % i == 0:
                #czynniki.append(i)
                j += 1
                while linie % i == 0:
                    linie = linie // i
            else:
                i += 2
            if j > 3:
                return False
        if j == 3:
            return True
        if j<3:
            return False

with open("liczby.txt", 'r') as plik:
    ile =0
    for linie in plik:
        linie = linie.strip()
        linie = int(linie)
        if czynniki(linie)==True:
            ile+=1
    print(ile)

