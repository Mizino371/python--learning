import tkinter as tk, random as r
from tkinter import PhotoImage
from tkinter import messagebox

class HraKolaciky:
    def __init__(self):
    
        self.root = tk.Tk()
        self.root.title("Kolačiky")
        self.c=tk.Canvas(width=920,height=420)
        self.c.pack()
        self.selfglobal_images = [PhotoImage(file=f"school projects/kružok/2. uloha/kolace/kolac{i}.png") for i in range(4)]
        self.predchadzajuci_vyber = {"kolac":None , "tanier":None}

        self.vyb_kol_x = 50
        self.vyb_kol_y = 350
        self.i = 1

        vyber_kolacov = r.randint(1,4)

        self.vstupny_text =c.create_text(150,380,text=f"Vyber {vyber_kolacov} koláčov z jednej sady.")

    # def vyherne_okno():
    #     root.title("Winner, winner, chicken winner")
    #     tkinter.Label(root, text="Vyhral si")

    def tanier_vyzobrazenie(self):
        x=50
        for i in range(3):
            sirka_strany = 240
            topy= 50
            boty = 230
            self.c.create_rectangle(x,topy,x+sirka_strany,boty,width=3)
            x+=sirka_strany + 50

    def klik_na_kolac(self,event):
        global i, vyb_kol_x
        self.kolac_id = self.event.widget.find_withtag("current")[0]
        self.info = self.c.gettags(kolac_id)
        
        if i >= vyber_kolacov:
            self.c.delete(self.vstupny_text)
            self.c.coords(self.kolac_id,vyb_kol_x,350)
            self.c.create_text(150,380,text="Vyhral si ")   
            messagebox.showinfo("vyhral si")
            
        
            
            
        elif self.predchadzajuci_vyber["kolac"] is None or (self.predchadzajuci_vyber["kolac"] == info[0] and predchadzajuci_vyber["tanier"] == info[1]):
            self.predchadzajuci_vyber["kolac"],self.predchadzajuci_vyber["tanier"] = info[0],info[1]
            self.c.coords(self.kolac_id,self.vyb_kol_x,350)
            self.vyb_kol_x +=50
            self.i +=1
            
        else:  
            self.c.create_text(150, 400,text="Vybral si zo zlej tácky alebo zlý koláč.Vyberaj z takej tácky ktorej si už pred tým vybral")

    

   
    def main(self):
        for tanier_id in range(3):
            for kolac_id in range(12):
                koalce_type= r.randint(0,3)
                kolac_img = self.global_images[koalce_type]
                y= 80 +(kolac_id % 3)* 60
                x= 80 +(kolac_id % 4)* 60 + (tanier_id % 3 * 290)
                zobrazenie_kolac = self.c.create_image(x,y, image = kolac_img)
                self.c.tag_bind(zobrazenie_kolac, "<Button-1>",self.klik_na_kolac)
                self.c.addtag_withtag(koalce_type,zobrazenie_kolac)
                self.c.addtag_withtag(tanier_id,zobrazenie_kolac)
                self.c.addtag_withtag(x,zobrazenie_kolac)
                self.c.addtag_withtag(y,zobrazenie_kolac)      
        
    def run(self):  
        self.root.mainloop()           
 
if __name__ == "__main__":
    game = HraKolaciky()
    game.run()
   












# paths = ["school projects/kružok/2. uloha/kolace/kolac{}.png".format(i) for i in range(4)]
# for path in paths:
#     img = PhotoImage(file=path)
#     global_images.append(img)


                      



# def vypocet(x):
#      y=85
#      for i in range(3):
#         Wx = x
#         for o in range(4):  
#             r_kolac_uno = r.choice(global_images)
#             prva_varka = c.create_image(Wx,y,image=r_kolac_uno)
#             Wx +=55
#         y+=55


# def imp_kolace():


#     prvy_tanier = ["school projects/kružok/2. uloha/kolace/kolac{}.png".format(i) for i in range(4)]
#     druhy_tanier = ["school projects/kružok/2. uloha/kolace/kolac{}.png".format(i) for i in range(4)]
#     treti_tanier = ["school projects/kružok/2. uloha/kolace/kolac{}.png".format(i) for i in range(4)]
#     for p in range(3):
#         if p ==0:

#             for path in prvy_tanier:
#                 vyber_random = r.choice(prvy_tanier)
#                 img = PhotoImage(file=vyber_random)
#                 global_images.append(img)
#                 vypocet(85)
#                 break
                

#         elif p==1:
#              for path in druhy_tanier:
#                 vyber_random = r.choice(druhy_tanier)
#                 img = PhotoImage(file=vyber_random)
#                 global_images.append(img)
#                 vypocet(375)
#                 break
                
#         elif p== 2:
#             for path in treti_tanier:
#                 vyber_random = r.choice(treti_tanier)
#                 img = PhotoImage(file=vyber_random)
#                 global_images.append(img)
#                 vypocet(670)
#                 break




  
# imp_kolace()



