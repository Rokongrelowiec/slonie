
def plik_wejsciowy():
    file = input("Podaj sciezke pliku wejsciowego: ")
    file = file.strip()
    plik = open(file, "r")
    text = plik.readlines()

    list = []
    for i in text:
        i = i.split()
        list.append(i)
    plik.close()

    '''
    list = lista z elementami
    list1 - ile sloni
    list2 - masy sloni
    list3 - kolejnosc ustawienia poczatkowa
    list4 - kolejnosc dyrektora
    '''

    list1 = [int(i) for i in list[0]]
    list2 = [int(i) for i in list[1]]
    list3 = [int(i)-1 for i in list[2]]  # numeracja od 0
    list4 = [int(i)-1 for i in list[3]]  # numeracja od 0

    # tworzymy permutacje - tablice N(ilosc sloni) elementow, ktora i tak potem zmieniamy
    permutacja = [i for i in range(list1[0])]

    # zmiana zawartosci permutacji
    for i in range(list1[0]):
        permutacja[list4[i]] = list3[i]

    from math import inf
    min_waga = inf


    for i in range(int(list1[0])):
        min_waga = min(list2[i], min_waga)

    tab = []
    for i in range(list1[0]):
        tab.append(False)

    wynik = 0


    for i in range(list1[0]):
        if not tab[i]:
            min_waga_cyklu = inf
            suma = 0
            aktaulny_cykl = i
            dlugosc_cyklu = 0
            while True:
                min_waga_cyklu = min(min_waga_cyklu, list2[aktaulny_cykl])
                suma += list2[aktaulny_cykl]
                aktaulny_cykl = permutacja[aktaulny_cykl]
                tab[aktaulny_cykl] = True
                dlugosc_cyklu += 1
                if aktaulny_cykl == i:
                    break
            wynik += min(suma+(dlugosc_cyklu-2)*min_waga_cyklu, suma+min_waga_cyklu+(dlugosc_cyklu+1)*min_waga)

    return wynik

def plik_wyjsciowy():
    file = input("Podaj sciezke pliku wyjsciowego(plik z wynikiem): ")
    plik = open(file, "r")
    text = plik.read()
    text = text.split()
    text = text[0]
    plik.close()
    return int(text)

