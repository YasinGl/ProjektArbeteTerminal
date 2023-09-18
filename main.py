class BankKonto:
    def __init__(self, namn, pin, saldo=0):
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
        return self.saldo #test
