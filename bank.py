import self

from bankkonto import BankKonto  # Importera BankKonto-klassen från bankkonto-modulen.

class Bank:  # Definiera Bank-klassen.
    def __init__(self):
        self.konton = {}
        # Ladda konton kommer att kallas direkt i main.py, så ingen anledning att anropa det här.

    def skapa_konto(self, namn, pin):
        kontonummer = len(self.konton) + 1
        self.konton[kontonummer] = BankKonto(namn, pin)

        # Automatiskt spara efter att ett konto har skapats
        self.spara_konton()
        return kontonummer

    def logga_in(self, kontonummer, pin):
        konto = self.konton.get(kontonummer)
        if konto and konto.pin == pin:
            return konto
        return None

    def ladda_konton(self):
        print("Försöker ladda information från databas...")  # Lägg till detta print-uttryck här.

        try:
            with open("konton.txt", "r") as f:
                for rad in f:
                    konto_nummer, namn, pin, saldo = rad.strip().split(",")
                    self.konton[int(konto_nummer)] = BankKonto(namn, pin, float(saldo))
            print("Information laddad från databas.")  # Lägg till detta print-uttryck här.
        except FileNotFoundError:
            print("konton.txt finns inte.")  # Lägg till detta print-uttryck här.

    def spara_konton(self):
        print("Försöker spara konton i databasen...")  # Lägg till detta print-uttryck här.

        with open("konton.txt", "w") as f:
            for konto_nummer, konto in self.konton.items():
                f.write(f"{konto_nummer},{konto.namn},{konto.pin},{konto.saldo}\n")

        print("Konton sparad i databasen.")  # Lägg till detta print-uttryck här.

