thank_you = "Dziękujemy za skorzystanie z programu :)"
blad_int = "Program akceptuje wyłącznie liczby całkowite!"
blad_ogolny = "Nastąpił błąd!"
bar = "-----"

while True:
    print("Witaj w kalkulatorze. Wybierz jedną z dostępnych operacji w polu poniżej.\n"
              "1. Dodawanie\n"
              "2. Odejmowanie\n"
              "3. Mnożenie\n"
              "4. Dzielenie\n"
              "5. Zakończ.")
    try:
        operacja = int(input("Wybierz działanie: "))
        if 1 <= operacja <=4:
            match operacja:

                case 1:
                    try:
                        a = int(input("Podaj liczbę A: "))
                        b = int(input("Podaj liczbę B: "))
                        dzialanie = a + b
                        print(f"Wynik dodawania: {dzialanie}")
                        print(bar)
                    except:
                        print(blad_int)

                case 2:
                    try:
                        a = int(input("Podaj liczbę A: "))
                        b = int(input("Podaj liczbę B: "))
                        dzialanie = a - b
                        print(f"Wynik odejmowania: {dzialanie}")
                        print(bar)
                    except:
                        print(blad_int)

                case 3:
                    try:
                        a = int(input("Podaj liczbę A: "))
                        b = int(input("Podaj liczbę B: "))
                        dzialanie = a * b
                        print(f"Wynik mnożenia: {dzialanie}")
                        print(bar)
                    except:
                        print(blad_int)

                case 4:
                    try:
                        a = int(input("Podaj liczbę A: "))
                        b = int(input("Podaj liczbę B: "))
                        dzialanie = a / b
                        print(f"Wynik dzielenia: {dzialanie}")
                        print(bar)
                    except:
                        print(blad_int)

            odp = input("Czy chcesz kontynuować? T/N ").strip().lower()
            if odp == "t":
                print(bar)
                continue
            elif odp != "t" and odp == "n":
                print(thank_you)
                break
            else:
                print(blad_ogolny)
                print("match")
                break

        elif operacja == 5:
            print(thank_you)
            break

        else:
            print("Nie rozpoznaję tej operacji.")
            odp = input("Czy chcesz kontynuować? T/N ").strip().lower()
            if odp == "t":
                print(bar)
                continue
            elif odp != "t" and odp == "n":
                print(thank_you)
                break
            else:
                print(blad_ogolny)
                print("if")
                break

    except:
            print(blad_ogolny, blad_int, "try")
            odp = input("Czy chcesz kontynuować? T/N ").strip().lower()
            if odp == "t":
                print(bar)
                continue
            elif odp != "t" and odp == "n":
                print(thank_you)
                break
            else:
                print(blad_ogolny)
                print("except")
                break


