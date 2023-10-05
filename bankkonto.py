class BankKonto:
    # Konstruktor för att initialisera ett bankkonto-objekt
    def __init__(self, namn, pin, saldo=0):
        # Instansvariabler för att lagra namn, pin-kod och saldo
        self.namn = namn  # Namnet på kontoinnehavaren
        self.pin = pin    # PIN-kod för kontot
        self.saldo = saldo  # Nuvarande saldo på kontot, standard är 0 om inget annat anges

    # Metod för att hantera insättningar till kontot
    def insattning(self, belopp):
        # Lägger till det insatta beloppet till det nuvarande saldot
        self.saldo += belopp
        # Returnerar det nya saldot
        return self.saldo

    # Metod för att hantera uttag från kontot
    def uttag(self, belopp):
        # Kontrollerar om det begärda uttagsbeloppet är större än det tillgängliga saldot
        if belopp > self.saldo:
            # Om ja, returnera ett felmeddelande
            return "Inte tillräckligt med pengar på kontot!"
        # Om nej, dra av det begärda beloppet från saldot
        self.saldo -= belopp
        # Returnerar det nya saldot
        return self.saldo

    # Metod för att visa det nuvarande saldot
    def visa_saldo(self):
        # Returnerar det nuvarande saldot
        return self.saldo
