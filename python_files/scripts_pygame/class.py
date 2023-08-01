class Ime:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def metoda(self):
        print(self.ime, self.prezime)

    def promeni_ime(self, novo_ime):
        self.ime = novo_ime

    @staticmethod
    def static_mehtod():
        print("static method")


ime = Ime("Pera", "Peric")
ime.metoda()
ime.promeni_ime("Mika")
ime.metoda()

Ime.static_mehtod()
