import tkinter as tk
from tkinter import PhotoImage
import random

class CrabGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Krabí hra")

        self.score = 0

        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.label_score = tk.Label(root, text="Skóre: 0")
        self.label_score.pack(pady=10)

        self.button_same = tk.Button(root, text="Rovnaké", command=self.check_same)
        self.button_same.pack(side=tk.LEFT, padx=10)

        self.button_different = tk.Button(root, text="Rôzne", command=self.check_different)
        self.button_different.pack(side=tk.RIGHT, padx=10)

        self.generate_crabs()
        self.update_score()

    def generate_crabs(self):
        crab_images = [PhotoImage(file="school projects/kružok/1. uloha/krab0.png"),
                       PhotoImage(file="school projects/kružok/1. uloha/krab1.png"),
                       PhotoImage(file = "school projects/kružok/1. uloha/krab2.png"),
                       PhotoImage(file = "school projects/kružok/1. uloha/krab3.png"),
                        PhotoImage(file = "school projects/kružok/1. uloha/krab4.png"),
                        PhotoImage(file = "school projects/kružok/1. uloha/krab5.png")]
        self.crab1_image = random.choice(crab_images)
        self.crab2_image = random.choice(crab_images)

        self.crab1 = self.canvas.create_image(100, 150, anchor=tk.CENTER, image=self.crab1_image)
        self.crab2 = self.canvas.create_image(300, 150, anchor=tk.CENTER, image=self.crab2_image)

    def check_same(self):
        if self.crab1 == self.crab2:
            self.score += 1
        else:
            self.score -= 10

        self.generate_crabs()
        self.update_score()

    def check_different(self):
        if self.crab1 != self.crab2:
            self.score += 1
        else:
            self.score -= 10

        self.generate_crabs()
        self.update_score()

    def update_score(self):
        self.label_score.config(text=f"Skóre: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = CrabGame(root)
    root.mainloop()
