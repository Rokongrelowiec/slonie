'''
Zadanie - Olimpiada Informatyczna 2008
Słonie

Treść: W ZOO ma się odbyć parada słoni, pracownicy początkowo ustawili słonie w danej kolejności.
       Jednakże dyrektor nie jest zadowolony z ustawienia pracowników, przez co proponuje swoje własne ustawienie.
       Wysiłek potrzebny do zamiany miejscami dwóch słoni jest równy sumie ich wag.
       Jaki jest minimalny wysiłek potrzebny do ustawienia słoni w kolejności podanej przez durektora?

dane wejsciowe:
    1 wiersz: ilosc sloni (numeracja poczawszy od 1)
    2 wersz: wagi kolejno slonii
    3 wiersz: kolejnosc poczatkowa
    4 wiersz: kolejnosc koncowa
dane wyjściowe:
    1 minimalny wysiłek
'''

# poniższe rozwiązanie zawiera wczytywanie pliku z danymi wejściowymi
# gdzie plik zawiera kolejno wiersze przedstawione w treści
# następnie dane są porównywane z plikiem z odpowiedzią, w rezultacie uzyskujemy logiczną odpowiedź: True or False


from Functions import *

# zestawienie w ladniejszej oprawie

def wyswietl_zestawienie():
    i = 0
    while True:
        i+=1
        try:
            res1 = plik_wejsciowy()
            res2 = plik_wyjsciowy()
            print(f"{i}. Wynik poprawny: {res2}, Moj wynik: {res1}, Porownanie(True/False): {res1==res2}")
        except FileNotFoundError as fnfe:
            print(fnfe)
        finally:
            koniec = input("Czy chcesz zakonczyc sprawdzanie? (T/N): ")
            koniec = (koniec.strip()).upper()
            if koniec == "T" or koniec == "TAK":
                break

wyswietl_zestawienie()


# tylko wyniki kolejno wypisane do danych wejsciowych
def wyswietl_tylko_wynik():
    try:
        res1 = plik_wejsciowy()
        print(res1)
    except:
        print("Nieprawidlowy plik!")

#wyswietl_tylko_wynik()

