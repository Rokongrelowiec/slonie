def wejscie():

    liczbaSloni = input("Liczba sloni: ")
    wagiSloni = input("Wagi sloni: ")
    ustawieniePoczatkowe = input("Ustawienie poczatkowe: ")
    ustawienieDyrektora = input("Ustawienie koncowe: ")

    liczbaSloni = int(liczbaSloni.strip())
    wagiSloni = wagiSloni.split()
    ustawieniePoczatkowe = ustawieniePoczatkowe.split()
    ustawienieDyrektora = ustawienieDyrektora.split()


    wagiSloni = [int(i) for i in wagiSloni]
    ustawieniePoczatkowe = [int(i)-1 for i in ustawieniePoczatkowe]  # numeracja od 0
    ustawienieDyrektora = [int(i)-1 for i in ustawienieDyrektora]  # numeracja od 0

    # tworzymy permutacje - tablice N(ilosc sloni) elementow, ktora i tak potem zmieniamy
    permutacja = [i for i in range(liczbaSloni)]

    # zmiana zawartosci permutacji
    for i in range(liczbaSloni):
        permutacja[ustawienieDyrektora[i]] = ustawieniePoczatkowe[i]

    from math import inf
    min_waga = inf


    for i in range(int(liczbaSloni)):
        min_waga = min(wagiSloni[i], min_waga)

    tab = []
    for i in range(liczbaSloni):
        tab.append(False)

    wynik = 0


    for i in range(liczbaSloni):
        if not tab[i]:
            min_waga_cyklu = inf
            suma = 0
            aktaulny_cykl = i
            dlugosc_cyklu = 0
            while True:
                min_waga_cyklu = min(min_waga_cyklu, wagiSloni[aktaulny_cykl])
                suma += wagiSloni[aktaulny_cykl]
                aktaulny_cykl = permutacja[aktaulny_cykl]
                tab[aktaulny_cykl] = True
                dlugosc_cyklu += 1
                if aktaulny_cykl == i:
                    break
            wynik += min(suma+(dlugosc_cyklu-2)*min_waga_cyklu, suma+min_waga_cyklu+(dlugosc_cyklu+1)*min_waga)

    return wynik



