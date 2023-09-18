from bankkonto import BankKonto # Importera BankKonto-klassen från bankkonto-modulen.


class Bank: # Definiera Bank-klassen.
    # Initiera Bank-objektet med en tom dictionary för att lagra bankkonton.
    def __init__(self):
        self.konton = {}

    def skapa_konto(self, namn, pin):     # Funktion för att skapa ett nytt konto.
        # Generera ett nytt kontonummer baserat på antalet befintliga konton.
        kontonummer = len(self.konton) + 1
        self.konton[kontonummer] = BankKonto(namn, pin)
        # Returnera det nya kontonumret.
        return kontonummer

    def logga_in(self, kontonummer, pin):
        konto = self.konton.get(kontonummer)
        if konto and konto.pin == pin:
            return konto
        return None
