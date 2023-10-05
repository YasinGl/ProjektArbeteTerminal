from bank import Bank  # Importera Bank-klassen från bank-modulen
import stdiomask  # först hade jag getpass men då märke jag att det blev helt dolt så jag bytte ut den mot mask

class TerminalColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def huvudmeny():  # Definiera huvudfunktionaliteten för programmet.
    bank = Bank()  # Initiera Bank-objektet.
    bank.ladda_konton()  # Ladda befintliga konton från konton.txt vid programstart.
    inloggad_konto = None  # Definiera en variabel för att hålla reda på inloggad användare.
    sagthej = False

    while True:     # Huvudloop för att köra programmet kontinuerligt.
        if not inloggad_konto:         # Om ingen användare är inloggad, visa huvudmenyn.
            print(f"{TerminalColors.HEADER}══════════════════════════════════════════════════════════")
            print(f"{TerminalColors.BLUE}Välkommen till YASINS Bank!{TerminalColors.ENDC}")
            print(f"{TerminalColors.HEADER}══════════════════════════════════════════════════════════")
            print(f"{TerminalColors.GREEN}1. Logga in{TerminalColors.ENDC}")
            print(f"{TerminalColors.GREEN}2. Skapa nytt konto{TerminalColors.ENDC}")
            print(f"{TerminalColors.GREEN}3. Avsluta{TerminalColors.ENDC}")
            try:
                val = int(input(f"{TerminalColors.BLUE}Vänligen välj ett alternativ (1-3): {TerminalColors.ENDC}"))
            except ValueError:  # KOllar invalid input
                print(f"{TerminalColors.FAIL}Ogiltigt val. Ange ett nummer mellan 1 och 3.{TerminalColors.ENDC}")
                continue  # går tillbaka till loopen och kör om

            if val == 1:             # Logga in-valet.
                kontonummer = stdiomask.getpass(f"{TerminalColors.BLUE}Ange ditt kontonummer: {TerminalColors.ENDC}", mask='*')
                try:
                    kontonummer = int(kontonummer)
                except ValueError:  # Hantera felaktig inmatning.
                    print(f"{TerminalColors.FAIL}Ogiltigt kontonummer. Ange endast siffror.{TerminalColors.ENDC}")
                    continue

                pin = stdiomask.getpass(f"{TerminalColors.BLUE}Ange ditt lösenord: {TerminalColors.ENDC}", mask='*')
                inloggad_konto = bank.logga_in(kontonummer, pin)
                if not inloggad_konto:
                    print(f"{TerminalColors.FAIL}Felaktiga inloggningsuppgifter!{TerminalColors.ENDC}")

            elif val == 2:             # Skapa nytt konto-valet.
                namn = input(f"{TerminalColors.BLUE}Ange ditt namn: {TerminalColors.ENDC}")
                pin = input(f"{TerminalColors.BLUE}Skapa ett lösenord: {TerminalColors.ENDC}")
                kontonummer = bank.skapa_konto(namn, pin)
                print(f"Ditt kontonummer är: {kontonummer}")

            elif val == 3:             # Avsluta programmet.
                break

        else:         # Om användaren är inloggad, visa alternativen för den inloggade användaren.
            if not sagthej:
                print(f"{TerminalColors.WARNING}Välkommen, {inloggad_konto.namn}!{TerminalColors.ENDC}")
                sagthej = True
            else:
                print(f"{TerminalColors.GREEN}(Inloggad) Bankkonto: {inloggad_konto.namn}{TerminalColors.ENDC}")
            print(f"{TerminalColors.GREEN}1. Sätt in pengar{TerminalColors.ENDC}")
            print(f"{TerminalColors.GREEN}2. Ta ut pengar{TerminalColors.ENDC}")
            print(f"{TerminalColors.GREEN}3. Visa saldo{TerminalColors.ENDC}")
            print(f"{TerminalColors.GREEN}4. Logga ut{TerminalColors.ENDC}")
            try:
                val = int(input(f"{TerminalColors.BLUE}Vänligen välj ett alternativ (1-4): {TerminalColors.ENDC}"))
            except ValueError:
                print(f"{TerminalColors.FAIL}Ogiltigt val. Ange ett nummer mellan 1 och 4.{TerminalColors.ENDC}")
                continue  # går tillbaka till loopen och kör om

            if val == 1:             # Sätt in pengar-valet.
                belopp = float(input(f"{TerminalColors.GREEN}Ange belopp att sätta in: {TerminalColors.ENDC}"))
                inloggad_konto.insattning(belopp)
                print(f"{TerminalColors.GREEN}Ditt nya saldo är: {inloggad_konto.visa_saldo()} :- {TerminalColors.ENDC}")
                bank.spara_konton()

            elif val == 2:              # Ta ut pengar-valet.
                belopp = float(input(f"{TerminalColors.GREEN}Ange belopp att ta ut: {TerminalColors.ENDC}"))
                resultat = inloggad_konto.uttag(belopp)
                if isinstance(resultat, str):  # Kontrollera om uttaget returnerade ett felmeddelande.
                    print(f"{TerminalColors.FAIL}{resultat}{TerminalColors.ENDC}")
                else:
                    print(f"{TerminalColors.GREEN}Ditt nya saldo är: {resultat} :- {TerminalColors.ENDC}")
                    bank.spara_konton()

            elif val == 3:             # Visa saldo-valet.
                print(f"{TerminalColors.GREEN}Ditt saldo är: {inloggad_konto.visa_saldo()} :- {TerminalColors.ENDC}")

            elif val == 4:             # Logga ut användaren.
                print(f"{TerminalColors.WARNING}Du har loggat ut, tack {inloggad_konto.namn} för att du använder Yasins Bank{TerminalColors.ENDC}")
                inloggad_konto = None
                sagthej = False

huvudmeny() # Kör huvudmenyn när scriptet körs.
