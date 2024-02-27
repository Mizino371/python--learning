import tkinter as tk 
from tkinter import messagebox
import random as r 
class slovicka_game:
    def __init__(self,root):
        self.root = root
        root.title("Translation Game")
    
        self.slovak_to_english = {

            
            "abandon": f"opustiť" "zanechať",
            "absurd": "absurdný",
            "accuse": "obviniť",
            "adapt": "prispôsobiť sa",
            "adolescent": "adolescent",
            "adoptive": "adoptívny",
            "agnostic": "agnostik",
            "altruistic": "altruisický",
            "angle": "uhol",
            "auction": "aukcia, dražba",
            "bill": "zákon, účet",
            "bookstall": "kníhkupectvo",
            "change": "zmena",
            "charity": "charita",
            "clinic": "klinika",
            "conditions": "podmienky",
            "contrary": "protiklad",
            "corporal": "telesný",
            "create": "vytvoriť",
            "creationist": "kreacionista",
            "decrease": "znížiť",
            "decide": "rozhodnúť",
            "echo": "ozvena",
            "equality": "rovnosť",
            "evolve": "vyvíjať sa",
            "expect": "očakávať",
            "expert": "expert",
            "force-feeding": "nútené kŕmenie",
            "gossip": "klebeta",
            "healer": "liečiteľ",
            "heresy": "kacírstvo, blud",
            "hereditary": "dedičný",
            "heroine": "hrdinka",
            "hips": "boky",
            "hunger strike": "hladovka",
            "hysteria": "hysterie",
            "in public": "na verejnosti",
            "incapable": "neschopný",
            "independently": "nezávisle",
            "individuality": "individualita",
            "influential": "vplyvný",
            "insomnia": "nespavosť",
            "intercept": "zachytiť, prerušiť",
            "join": "pripojiť sa",
            "manipulative": "manipulatívny",
            "mercy": "milosrdenstvo",
            "method": "metóda",
            "migration": "migrácia",
            "militant": "militantný",
            "motivation": "motivácia",
            "natural selection": "prírodný výber",
            "notion": "názor, myšlienka",
            "oppose": "protiviť sa",
            "originate": "vzniknúť",
            "password": "heslo",
            "persuade": "presvedčiť",
            "planet": "planéta",
            "presenter": "moderátor",
            "process": "proces",
            "promotion": "povýšenie",
            "protest": "protestovať, namietnutie",
            "put forward": "navrhnúť",
            "railings": "zábradlie",
            "rain down": "pršať",
            "rational": "racionálny",
            "recommend": "odporučiť",
            "recording studio": "nahrávacie štúdio",
            "reputation": "povesť",
            "rhythm": "rytmus",
            "right vs. wrong": "pravda proti nepravosti",
            "right-wing": "pravicový",
            "riot": "vzbura, nepokoje",
            "rotate": "otáčať sa",
            "screen": "obrazovka",
            "sexism": "sexismus",
            "shame": "hanba",
            "simple": "jednoduchý",
            "slash": "škrtnúť, zraziť",
            "spill": "vyliať",
            "standstill": "zastavenie, stoj",
            "struggle": "zápas, boj",
            "suffragette": "sufražetka",
            "suit": "padnúť, hodiť sa",
            "telescope": "ďalekohľad",
            "theory": "teória",
            "unaware of": "nevedomý si",
            "unworkable": "nefunkčný, nepraktický"
        }
        
        self.aktualne_slovak_world, self.aktualne_english_world = r.choice(list(self.slovak_to_english.items()))
        
        lvl1_Lab = tk.Label(text=f"{self.aktualne_slovak_world}", font="Arial")

        lvl1_Lab.place(y=150, x=290)
        root = tk.Tk()
        self.odpoved = tk.Entry(root)

         
        self.odpoved.pack(pady=20)

    def chceck(self):
        if self.odpoved.get() == self.aktualne_english_world:
            messagebox.showinfo("Correct", "Correct")
        else:
            messagebox.showinfo("Wrong", "Wrong")


    def next(self):
        self.aktualne_slovak_world, self.aktualne_english_world = r.choice(list(self.slovak_to_english.items()))
        lvl1_Lab = tk.Label(text=f"{self.aktualne_slovak_world}", font="Arial")
        lvl1_Lab.place(y=150, x=290)
        self.odpoved.delete(0, "end")
        self.odpoved.pack(pady=20)
        self.odpoved.focus_set()
        self.odpoved.bind("<Return>", self.chceck)
    
    def main(self):
        self.odpoved.focus_set()
        self.odpoved.bind("<Return>", self.chceck)
        self.odpoved.bind("<Return>", self.next)
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    slovicka_game(root).main()
    root.mainloop()