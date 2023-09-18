from bank import Bank

def huvudmeny():
    bank = Bank()
    inloggad_konto = None

    while True:
        if not inloggad_konto:
            print("Välkommen till YASIN Bank!")
            print("1. Logga in")
            print("2. Skapa nytt konto")
            print("3. Avsluta")
            val = int(input("Vänligen välj ett alternativ (1-3): "))

            if val == 1:
                try:
                    kontonummer = int(input("Ange ditt kontonummer: "))
                except ValueError:
                    print("Ogiltigt kontonummer. Ange endast siffror.")
                    continue

                pin = input("Ange ditt lösenord: ")
                inloggad_konto = bank.logga_in(kontonummer, pin)
                if not inloggad_konto:
                    print("Felaktiga inloggningsuppgifter!")


            elif val == 2:
                namn = input("Ange ditt namn: ")
                pin = input("Skapa ett lösenord: ")
                kontonummer = bank.skapa_konto(namn, pin)
                print(f"Ditt kontonummer är: {kontonummer}")

            elif val == 3:
                break

        else:
            print(f"Välkommen {inloggad_konto.namn}!")
            print("1. Sätt in pengar")
            print("2. Ta ut pengar")
            print("3. Visa saldo")
            print("4. Logga ut")
            val = int(input("Vänligen välj ett alternativ (1-4): "))

            if val == 1:
                belopp = float(input("Ange belopp att sätta in: "))
                inloggad_konto.insattning(belopp)
                print(f"Ditt nya saldo är: {inloggad_konto.visa_saldo()}")

            elif val == 2:
                belopp = float(input("Ange belopp att ta ut: "))
                resultat = inloggad_konto.uttag(belopp)
                if isinstance(resultat, str):
                    print(resultat)
                else:
                    print(f"Ditt nya saldo är: {resultat}")

            elif val == 3:
                print(f"Ditt saldo är: {inloggad_konto.visa_saldo()}")

            elif val == 4:
                inloggad_konto = None
huvudmeny()
