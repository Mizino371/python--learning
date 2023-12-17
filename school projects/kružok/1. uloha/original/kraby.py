import tkinter as tk, random
from tkinter import PhotoImage



class kraby:
    def __init__(self,root):
        self.root = root
        self.root.title("Krabia hra")

        self.score = 0

        self.c=tk.Canvas(width=600,height=400)
        self.c.pack()

        self.label_score = tk.Label(root,text= "skóre = 0")
        self.label_score.pack(pady=20)

        spol_f = ("Helvica", 12)

        self.button_rovnake = tk.Button(text="Rovnaké", command=self.kontrola_rovnake, bg="Orange", font=spol_f)
        self.button_rovnake.pack(side=tk.LEFT , padx=25,)

        self.button_odlisne = tk.Button(text="Odlišné",command=self.kontrola_odlisne,bg= "light blue", font=spol_f)
        self.button_odlisne.pack(side= tk.RIGHT,padx=25)

        self.generate_crabs()
        self.update_score()

    def generate_crabs(self):
        crab_images = [ PhotoImage(file = "school projects/kružok/1. uloha/krab0.png"),
                        PhotoImage(file = "school projects/kružok/1. uloha/krab1.png"),
                        PhotoImage(file = "school projects/kružok/1. uloha/krab2.png"),
                        PhotoImage(file = "school projects/kružok/1. uloha/krab3.png"),
                        PhotoImage(file = "school projects/kružok/1. uloha/krab4.png"),
                        PhotoImage(file = "school projects/kružok/1. uloha/krab5.png")]
        self.crab1_image = random.choice(crab_images)
        self.crab2_image = random.choice(crab_images)

        self.crab1 = self.c.create_image(150, 200, anchor=tk.CENTER, image=self.crab1_image)
        self.crab2 = self.c.create_image(450, 200, anchor=tk.CENTER, image=self.crab2_image)

    def kontrola_rovnake(self):
        if self.crab1_image==self.crab2_image:
            self.score += 1
        else:
            
            self.score -=10

        self.generate_crabs()
        self.update_score()
    
    
    def kontrola_odlisne(self):
        if self.crab1_image != self.crab2_image:
            self.score += 1
        else:
            self.score -= 10
    
        self.generate_crabs()
        self.update_score()
        
    def update_score(self):
        self.label_score.config(text = f"Skóre: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = kraby(root)
    root.mainloop()
    

    