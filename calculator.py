cont = ("T")
thank_you = ("Dziękujemy za skorzystanie z programu :)")
blad_ogolny = ("Nastąpił błąd!")
bar = ("-----")

while cont:

    print("Witaj w kalkulatorze. Wybierz jedną z dostępnych operacji w polu poniżej.\n"
          "1. Dodawanie\n"
          "2. Odejmowanie\n"
          "3. Mnożenie\n"
          "4. Dzielenie\n"
          "5. Zakończ.")
    try:
        operacja = int(input("Wybierz działanie: "))
        match operacja:
            case 1:
                a = int(input("Podaj liczbę A: "))
                b = int(input("Podaj liczbę B: "))
                dzialanie = a + b
                print(f"Wynik dodawania: {dzialanie}")
                print(bar)
                cont = input("Czy kontynuować? T/N: ").lower()
                if cont == "t":
                    print()
                    continue
                elif cont == "n":
                    print(thank_you)
                    break
                else:
                    print(blad_ogolny)
                    break
            case 2:
                a = int(input("Podaj liczbę A: "))
                b = int(input("Podaj liczbę B: "))
                dzialanie = a - b
                print(f"Wynik odejmowania: {dzialanie}")
                cont = input("Czy kontynuować? T/N: ").lower()
                print(bar)
                cont = input("Czy kontynuować? T/N: ").lower()
                if cont == "t":
#dowiedz sie, dlaczego w tym miejscu nie działa
                    print()
                    continue
                elif cont == "n":
                    print(thank_you)
                    break
                else:
                    print(blad_ogolny)
                    break
            case 3:
                a = int(input("Podaj liczbę A: "))
                b = int(input("Podaj liczbę B: "))
                dzialanie = a * b
                print(f"Wynik mnożenia: {dzialanie}")
                print(bar)
                cont = input("Czy kontynuować? T/N: ").lower()
                if cont == "t":
                    print()
                    continue
                elif cont == "n":
                    print(thank_you)
                    break
                else:
                    print(blad_ogolny)
                    break
            case 4:
                try:
                    a = int(input("Podaj liczbę A: "))
                    b = int(input("Podaj liczbę B: "))
                    dzialanie = a / b
                    print(f"Wynik dzielenia: {dzialanie}")
                    print(bar)
                    cont = input("Czy kontynuować? T/N: ").lower()
                    if cont == "t":
                        print()
                        continue
                    elif cont == "n":
                        print(thank_you)
                        break
                    else:
                        print(blad_ogolny)
                        break
                except ZeroDivisionError as zero_error:
                    print(zero_error)
                    print("Nie wolno dzielić przez 0!")
    except:
        print("Używaj tylko liczb całkowitych!")
    match operacja:
        case 5:
            print(thank_you)
            exit()
        case _:
            print("Nie ma takiej operacji, spróbuj ponownie.")

