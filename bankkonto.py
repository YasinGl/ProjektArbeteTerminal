class BankKonto: # Definiera klassen BankKonto.
    def __init__(self, namn, pin, saldo=0):     # Initialisera ett BankKonto-objekt med namn, pin och ett inledande saldo (standardvärde är 0).
        self.namn = namn  # Namnet på kontoinnehavaren.
        self.pin = pin # Pin-kod för kontot.
        self.saldo = saldo # Det aktuella saldot på kontot.

    def insattning(self, belopp):     # Metod för att sätta in pengar på kontot.
        self.saldo += belopp # Lägg till det angivna beloppet till saldot.
        return self.saldo # Returnera det uppdaterade saldot

    def uttag(self, belopp):     # Metod för att göra ett uttag från kontot.
        if belopp > self.saldo:         # Kontrollera om det angivna beloppet överstiger det aktuella saldot.
            return "Inte tillräckligt med pengar på kontot!"             # Om det inte finns tillräckligt med pengar, returnera ett felmeddelande.
        self.saldo -= belopp         # Dra bort det angivna beloppet från saldot.
        return self.saldo         # Returnera det uppdaterade saldot.

    def visa_saldo(self):     # Metod för att visa det aktuella saldot på kontot.
        return self.saldo
