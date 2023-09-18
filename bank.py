from bankkonto import BankKonto # Importera BankKonto-klassen från bankkonto-modulen.


class Bank: # Definiera Bank-klassen.
    # Initiera Bank-objektet med en tom dictionary för att lagra bankkonton.
    def __init__(self):
        self.konton = {}

    def skapa_konto(self, namn, pin):     # Funktion för att skapa ett nytt konto.
        # Generera ett nytt kontonummer baserat på antalet befintliga konton.
        kontonummer = len(self.konton) + 1         # Skapa ett nytt BankKonto-objekt och lagra det i dictionary med kontonummer som nyckel.
        self.konton[kontonummer] = BankKonto(namn, pin)
        # Returnera det nya kontonumret.
        return kontonummer

    def logga_in(self, kontonummer, pin):     # Funktion för att logga in på ett befintligt konto.
        konto = self.konton.get(kontonummer)         # Hämta konto baserat på givet kontonummer.
        if konto and konto.pin == pin:         # Kontrollera om kontot existerar och om PIN-koden stämmer överens.
            return konto
        return None         # Om inloggningen misslyckas, returnera None.

