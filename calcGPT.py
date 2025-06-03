thank_you = "Dziękujemy za skorzystanie z programu :)"
blad_int = "Program akceptuje wyłącznie liczby całkowite!"
blad_ogolny = "Nastąpił błąd!"
bar = "-----"

def pobierz_liczby():
    try:
        a = int(input("Podaj liczbę A: "))
        b = int(input("Podaj liczbę B: "))
        return a, b
    except ValueError:
        print(blad_int)
        return None

def czy_kontynuowac():
    odp = input("Czy chcesz kontynuować? T/N ").strip().lower()
    if odp == "t":
        print(bar)
        return True
    elif odp == "n":
        print(thank_you)
        return False
    else:
        print(blad_ogolny)
        return False

while True:
    print("Witaj w kalkulatorze. Wybierz jedną z dostępnych operacji:\n"
          "1. Dodawanie\n"
          "2. Odejmowanie\n"
          "3. Mnożenie\n"
          "4. Dzielenie\n"
          "5. Zakończ.")

    try:
        operacja = int(input("Wybierz działanie: "))

        if operacja == 5:
            print(thank_you)
            break

        elif operacja in (1, 2, 3, 4):
            liczby = pobierz_liczby()
            if not liczby:
                if not czy_kontynuowac():
                    break
                continue

            a, b = liczby
            if operacja == 1:
                print(f"Wynik dodawania: {a + b}")
            elif operacja == 2:
                print(f"Wynik odejmowania: {a - b}")
            elif operacja == 3:
                print(f"Wynik mnożenia: {a * b}")
            elif operacja == 4:
                try:
                    print(f"Wynik dzielenia: {a / b}")
                except ZeroDivisionError:
                    print("Nie można dzielić przez zero!")

            print(bar)
            if not czy_kontynuowac():
                break

        else:
            print("Nie rozpoznaję tej operacji.")
            if not czy_kontynuowac():
                break

    except ValueError:
        print(f"{blad_ogolny} {blad_int}")
        if not czy_kontynuowac():
            break
