class BankKonto:
    def __init__(self, namn, pin, saldo = 0):
        self.namn = namn
        self.pin = pin
        self.saldo = saldo

    def insattning(self, belopp):
        self.saldo += belopp
        return self.saldo

    def uttag(self, belopp):
        if belopp > self.saldo:
            return "Inte tillräckligt med pengar på kontot!"
        self.saldo -= belopp
        return self.saldo

    def visa_saldo(self):
        return self.saldo


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

