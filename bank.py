from bankkonto import BankKonto

class Bank:
    def __init__(self):
        self.konton = {}

    def skapa_konto(self, namn, pin):
        kontonummer = len(self.konton) + 1
        self.konton[kontonummer] = BankKonto(namn, pin)
        return kontonummer

    def logga_in(self, kontonummer, pin):
        konto = self.konton.get(kontonummer)
        if konto and konto.pin == pin:
            return konto
        return None
