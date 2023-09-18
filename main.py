from bank import Bank # Importera Bank-klassen från bank-modulen.


def huvudmeny(): # Definiera huvudfunktionaliteten för programmet.
    bank = Bank()     # Initiera Bank-objektet.
    inloggad_konto = None     # Definiera en variabel för att hålla reda på inloggad användare.


    while True:     # Huvudloop för att köra programmet kontinuerligt.
        if not inloggad_konto:         # Om ingen användare är inloggad, visa huvudmenyn.
            print("Välkommen till YASIN Bank!")
            print("1. Logga in")
            print("2. Skapa nytt konto")
            print("3. Avsluta")
            val = int(input("Vänligen välj ett alternativ (1-3): "))

            if val == 1:             # Logga in-valet.
                try:
                    kontonummer = int(input("Ange ditt kontonummer: "))
                except ValueError:  # Hantera felaktig inmatning.
                    print("Ogiltigt kontonummer. Ange endast siffror.")
                    continue

                pin = input("Ange ditt lösenord: ")
                inloggad_konto = bank.logga_in(kontonummer, pin)
                if not inloggad_konto:
                    print("Felaktiga inloggningsuppgifter!")


            elif val == 2:             # Skapa nytt konto-valet.
                namn = input("Ange ditt namn: ")
                pin = input("Skapa ett lösenord: ")
                kontonummer = bank.skapa_konto(namn, pin)
                print(f"Ditt kontonummer är: {kontonummer}")

            elif val == 3:             # Avsluta programmet.
                break

        else:         # Om användaren är inloggad, visa alternativen för den inloggade användaren.
            print(f"Välkommen {inloggad_konto.namn}!")
            print("1. Sätt in pengar")
            print("2. Ta ut pengar")
            print("3. Visa saldo")
            print("4. Logga ut")
            val = int(input("Vänligen välj ett alternativ (1-4): "))

            if val == 1:             # Sätt in pengar-valet.
                belopp = float(input("Ange belopp att sätta in: "))
                inloggad_konto.insattning(belopp)
                print(f"Ditt nya saldo är: {inloggad_konto.visa_saldo()}")

            elif val == 2:              # Ta ut pengar-valet.
                belopp = float(input("Ange belopp att ta ut: "))
                resultat = inloggad_konto.uttag(belopp)
                if isinstance(resultat, str):  # Kontrollera om uttaget returnerade ett felmeddelande.
                    print(resultat)
                else:
                    print(f"Ditt nya saldo är: {resultat}")

            elif val == 3:
                print(f"Ditt saldo är: {inloggad_konto.visa_saldo()}")

            elif val == 4:
                inloggad_konto = None
huvudmeny()
