class BankKonto: # Definiera klassen BankKonto.
    def __init__(self, namn, pin, saldo=0):     # Initialisera ett BankKonto-objekt med namn, pin och ett inledande saldo (standardvärde är 0).
        self.namn = namn  # Namnet på kontoinnehavaren.
        self.pin = pin # Pin-kod för kontot.
        self.saldo = saldo # Det aktuella saldot på kontot.

    def insattning(self, belopp):
        self.saldo += belopp
        return self.saldo

    def uttag(self, belopp):
        if belopp > self.saldo:
            return "Inte tillräckligt med pengar på kontot!"
        self.saldo -= belopp
        return self.saldo

    def visa_saldo(self):     # Metod för att visa det aktuella saldot på kontot.
        return self.saldo
