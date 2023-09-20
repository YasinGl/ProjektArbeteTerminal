from bank import Bank # Importera Bank-klassen från bank-modulen.
import stdiomask

# ordnar så att inmating som inte blir synlig

class TerminalColors:
    BLUE = '\033[94m'
    FAIL = '\033[91m'
    SLUTVANLIG = '\033[0m'
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
            print(f"{TerminalColors.BLUE}Välkommen till Yasins Bank!{TerminalColors.SLUTVANLIG}")
            print(f"{TerminalColors.CYAN} 1. Logga in {TerminalColors.SLUTVANLIG}")
            print(f" {TerminalColors.CYAN}2. Skapa nytt konto {TerminalColors.SLUTVANLIG}")
            print(f"{TerminalColors.CYAN} 3. Avsluta {TerminalColors.SLUTVANLIG}")
            try:
                val = int(input(f"{TerminalColors.BLUE}Vänligen välj ett alternativ (1-3): {TerminalColors.SLUTVANLIG}"))
            except ValueError:  # KOllar invalid input
                print(f"{TerminalColors.FAIL}Ogiltigt val. Ange ett nummer mellan 1 och 3.{TerminalColors.SLUTVANLIG}")
                continue  # går tillbaka till loopen och kör om

            if val == 1:             # Logga in-valet.
                try:
                    kontonummer = stdiomask.getpass(f"{TerminalColors.BLUE}Ange ditt kontonummer: {TerminalColors.SLUTVANLIG}", mask='*')
                    kontonummer = int(kontonummer)
         # getpass används i vissa terminalmiljöer som inte stöder ekofri inmatning. Detta är särskilt vanligt när du kör kod i vissa IDE:er, som PyCharm
                #Där standardterminalfunktionaltet inte används därför fungerar inte koden här men fungerar i en exe fil
                except ValueError:  # Hantera felaktig inmatning.
                    print(f"{TerminalColors.FAIL}Ogiltigt kontonummer. Ange endast siffror.{TerminalColors.SLUTVANLIG}")
                    continue

                    #jag har använt mig av funktionen getpass men den stöds inte av pycharm eftersom pycharm in stödjer eko fri inmatning
                    #

                pin = stdiomask.getpass(f"{TerminalColors.BLUE}Ange ditt lösenord: {TerminalColors.SLUTVANLIG}",mask='*1')
                inloggad_konto = bank.logga_in(kontonummer, pin)
                if not inloggad_konto:
                    print(f"{TerminalColors.FAIL}Felaktiga inloggningsuppgifter!{TerminalColors.SLUTVANLIG}")

            elif val == 2:             # Skapa nytt konto-valet.
                namn = input(f"{TerminalColors.BLUE}Ange ditt namn: {TerminalColors.SLUTVANLIG}")
                pin = input(f"{TerminalColors.BLUE}Skapa ett lösenord: {TerminalColors.SLUTVANLIG}")
                kontonummer = bank.skapa_konto(namn, pin)
                print(f"Ditt kontonummer är: {kontonummer}")

            elif val == 3:             # Avsluta programmet.
                break

        else:         # Om användaren är inloggad, visa alternativen för den inloggade användaren.
            print(f"{TerminalColors.GUL}Välkommen {TerminalColors.SLUTVANLIG} {TerminalColors.LILA}{inloggad_konto.namn}!{TerminalColors.LILA}")
            print(f"{TerminalColors.CYAN}1. Sätt in pengar{TerminalColors.SLUTVANLIG}")
            print(f"{TerminalColors.CYAN}2. Ta ut pengar{TerminalColors.SLUTVANLIG}")
            print(f"{TerminalColors.CYAN}3. Visa saldo{TerminalColors.SLUTVANLIG}")
            print(f"{TerminalColors.CYAN}4. Logga ut{TerminalColors.SLUTVANLIG}")
            try:
                val = int(input(f"{TerminalColors.BLUE}Vänligen välj ett alternativ (1-4): {TerminalColors.SLUTVANLIG}"))
            except ValueError:
                print(f"{TerminalColors.FAIL}Ogiltigt val. Ange ett nummer mellan 1 och 4.{TerminalColors.SLUTVANLIG}")
                continue  # går tillbaka till loopen och kör om

            if val == 1:             # Sätt in pengar-valet.
                belopp = float(input(f"{TerminalColors.OKGREEN}Ange belopp att sätta in: {TerminalColors.SLUTVANLIG}"))
                inloggad_konto.insattning(belopp)
                print(f"Ditt nya saldo är: {inloggad_konto.visa_saldo()} :-")
                bank.spara_konton()

            elif val == 2:              # Ta ut pengar-valet.
                belopp = float(input(f"{TerminalColors.OKGREEN}Ange belopp att ta ut: {TerminalColors.SLUTVANLIG}"))
                resultat = inloggad_konto.uttag(belopp)
                if isinstance(resultat, str):  # Kontrollera om uttaget returnerade ett felmeddelande.
                    print(f"{TerminalColors.FAIL}{resultat}{TerminalColors.SLUTVANLIG}")
                else:
                    print(f"Ditt nya saldo är: {resultat} :-")
                    bank.spara_konton()

            elif val == 3:             # Visa saldo-valet.
                print(f" {TerminalColors.OKGREEN} Ditt saldo är: {inloggad_konto.visa_saldo()} :- {TerminalColors.SLUTVANLIG}")

            elif val == 4:             # Logga ut användaren.
                inloggad_konto = None
                print(f"{TerminalColors.GUL}Du har loggat ut, tack för att du använder Yasins Bank{TerminalColors.SLUTVANLIG}")

huvudmeny() # Kör huvudmenyn när scriptet körs.
