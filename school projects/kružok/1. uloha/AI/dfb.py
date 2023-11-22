class Auto:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model
        self.stav = "novy"

    def popis(self):
        return f"{self.znacka} {self.model}, stav: {self.stav}"

# Vytvorenie novej inštancie triedy Auto a automatické volanie metódy __init__
moje_auto = Auto(znacka="Toyota", model="Corolla")

# Volanie metódy popis
print(moje_auto.popis())  # Vypíše: Toyota Corolla, stav: novy
