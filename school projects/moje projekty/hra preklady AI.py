import tkinter as tk
from tkinter import messagebox
import random


class TranslationGame:
    def __init__(self, master):
        self.master = master
        self.c=tk.Canvas()
        self.c.pack()

        master.title("Translation Game")

        # Slovník slovíčok a ich prekladov
        self.slovak_to_english = {
            "opustiť, zanechať": "abandon",
            "absurdný": "absurd",
            "obviniť": "accuse",
            "prispôsobiť sa": "adapt",
            "adolescent": "adolescent",
            "adoptívny": "adoptive",
            "agnostik": "agnostic",
            "altruisický": "altruistic",
            "uhol": "angle",
            "aukcia, dražba": "auction",
            "hladovka": "hunger strike",
            "hysterie": "hysteria",
            "na verejnosti": "in public",
            "neschopný": "incapable",
            # ... a tak ďalej
            "nefunkčný, nepraktický": "unworkable"
        }

        self.score = 0
        self.current_slovak_word, self.current_english_word = random.choice(list(self.slovak_to_english.items()))

        # rozhranie
        self.label = tk.Label(master, text=f"Prelož slovo: '{self.current_slovak_word}'")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Odpovedať", command=self.check_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(master, text="Skóre: 0")
        self.score_label.pack()

    def check_answer(self):
        answer = self.entry.get().strip().lower()

        if answer == self.current_english_word:
            self.score += 1
            messagebox.showinfo("Výsledok", "Správne! +1 bod")
        else:
            self.score -= 2
            messagebox.showerror("Výsledok", f"Nesprávne! -2 body. Správna odpoveď bola: {self.current_english_word}")

        if self.score >= 60:
            messagebox.showinfo("Gratulujeme!", "Dosiahol si 60 bodov!")
            self.master.destroy()
        else:
            self.score_label.config(text=f"Skóre: {self.score}")
            self.new_word()

    def new_word(self):
        self.current_slovak_word, self.current_english_word = random.choice(list(self.slovak_to_english.items()))
        self.label.config(text=f"Prelož slovo: '{self.current_slovak_word}'")
        self.entry.delete(0, tk.END)

    
root = tk.Tk()
my_game = TranslationGame(root)
root.mainloop()


