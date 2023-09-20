from bank import Bank # Importera Bank-klassen från bank-modulen.
import getpass # ordnar så att inmating som inte blir synlig

class TerminalColors:
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OKGREEN = '\033[92m'
    CYAN = '\033[36m'
    GUL = '\033[93m'
    LILA = '\033[35m'

def huvudmeny():  # Definiera huvudfunktionaliteten för programmet.
    bank = Bank()  # Initiera Bank-objektet.
    bank.ladda_konton()  # Ladda befintliga konton från konton.txt vid programstart.
    inloggad_konto = None  # Definiera en variabel för att hålla reda på inloggad användare.

    while True:     # Huvudloop för att köra programmet kontinuerligt.
        if not inloggad_konto:         # Om ingen användare är inloggad, visa huvudmenyn.
            print(f"{TerminalColors.OKBLUE}Välkommen till Yasins Bank!{TerminalColors.ENDC}")
            print(f"{TerminalColors.CYAN} 1. Logga in {TerminalColors.ENDC}")
            print(f" {TerminalColors.CYAN}2. Skapa nytt konto {TerminalColors.ENDC}")
            print(f"{TerminalColors.CYAN} 3. Avsluta {TerminalColors.ENDC}")
            try:
                val = int(input(f"{TerminalColors.OKBLUE}Vänligen välj ett alternativ (1-3): {TerminalColors.ENDC}"))
            except ValueError:  # KOllar invalid input
                print(f"{TerminalColors.FAIL}Ogiltigt val. Ange ett nummer mellan 1 och 3.{TerminalColors.ENDC}")
                continue  # går tillbaka till loopen och kör om

            if val == 1:             # Logga in-valet.
                try:
                    kontonummer = getpass.getpass(f"{TerminalColors.OKBLUE}Ange ditt kontonummer: {TerminalColors.ENDC}")
                    kontonummer = int(kontonummer)
                except ValueError:  # Hantera felaktig inmatning.
                    print(f"{TerminalColors.FAIL}Ogiltigt kontonummer. Ange endast siffror.{TerminalColors.ENDC}")
                    continue

                pin = input(f"{TerminalColors.OKBLUE}Ange ditt lösenord: {TerminalColors.ENDC}")
                inloggad_konto = bank.logga_in(kontonummer, pin)
                if not inloggad_konto:
                    print(f"{TerminalColors.FAIL}Felaktiga inloggningsuppgifter!{TerminalColors.ENDC}")

            elif val == 2:             # Skapa nytt konto-valet.
                namn = input(f"{TerminalColors.OKBLUE}Ange ditt namn: {TerminalColors.ENDC}")
                pin = input(f"{TerminalColors.OKBLUE}Skapa ett lösenord: {TerminalColors.ENDC}")
                kontonummer = bank.skapa_konto(namn, pin)
                print(f"Ditt kontonummer är: {kontonummer}")

            elif val == 3:             # Avsluta programmet.
                break

        else:         # Om användaren är inloggad, visa alternativen för den inloggade användaren.
            print(f"{TerminalColors.GUL}Välkommen {TerminalColors.ENDC} {TerminalColors.LILA}{inloggad_konto.namn}!{TerminalColors.LILA}")
            print(f"{TerminalColors.CYAN}1. Sätt in pengar{TerminalColors.ENDC}")
            print(f"{TerminalColors.CYAN}2. Ta ut pengar{TerminalColors.ENDC}")
            print(f"{TerminalColors.CYAN}3. Visa saldo{TerminalColors.ENDC}")
            print(f"{TerminalColors.CYAN}4. Logga ut{TerminalColors.ENDC}")
            val = int(input(f"{TerminalColors.OKBLUE}Vänligen välj ett alternativ (1-4): {TerminalColors.ENDC}"))

            if val == 1:             # Sätt in pengar-valet.
                belopp = float(input(f"{TerminalColors.OKGREEN}Ange belopp att sätta in: {TerminalColors.ENDC}"))
                inloggad_konto.insattning(belopp)
                print(f"Ditt nya saldo är: {inloggad_konto.visa_saldo()} :-")
                bank.spara_konton()

            elif val == 2:              # Ta ut pengar-valet.
                belopp = float(input(f"{TerminalColors.OKGREEN}Ange belopp att ta ut: {TerminalColors.ENDC}"))
                resultat = inloggad_konto.uttag(belopp)
                if isinstance(resultat, str):  # Kontrollera om uttaget returnerade ett felmeddelande.
                    print(f"{TerminalColors.FAIL}{resultat}{TerminalColors.ENDC}")
                else:
                    print(f"Ditt nya saldo är: {resultat} :-")
                    bank.spara_konton()

            elif val == 3:             # Visa saldo-valet.
                print(f" {TerminalColors.OKGREEN} Ditt saldo är: {inloggad_konto.visa_saldo()} :- {TerminalColors.ENDC}")

            elif val == 4:             # Logga ut användaren.
                inloggad_konto = None
                print(f"{TerminalColors.OKBLUE}Du har loggat ut, tack för att du använder Yasins Bank{TerminalColors.ENDC}")

huvudmeny() # Kör huvudmenyn när scriptet körs.
