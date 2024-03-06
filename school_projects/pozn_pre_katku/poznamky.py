import tkinter, random
canvas = tkinter.Canvas()
canvas.pack()



def štvorec (suradnice):        # def pomenovanie skupiny funkcií (suradnice):
		x=suradnice.x           #Tieto dva riadky proste stále sú také isté
		y=suradnice.y
		canvas.create_rectangle(x,y,x+200,y+200)                        #Ďalej pokračuješ v programe ktorý chceš vytvoriť si

canvas.bind("<Button-3>", štvorec)          #tlačidlo na myši ktoré po stlačení niečo urobí 
canvas.bind_all("<m>",štvorec)              #tlačidlo na klavesnici ktoré po stlačení niečo urobí

canvas.create_line(100,100,200,200, tags="čiara") #tags ---> pomocou tags pridáš funkciu ako canvas.create_line/oval/rectangle...
                                                  # do skupiny. tags = "názov skupiny (Pr. čiara)", 
                                                  # tentto tag možeš použit pri posúvaní 
                                                  #S canvas.move() (ďalej vysvetlím kde to napíšeš)


canvas.move("čiara",5,5)                    #canvas.move(názov_skupiny_funkcií / tags ,posun o nejakú hodnotu na x,
                                            # posun o nejakú hodnotu na y,)
                                            #Vďaka canvas.move() nemusíš pri nejakej animácií mazať a znova vytvárať objekt,
                                            # pomocou tags alebo def nazov_funkcie, 
                                            # toho vieš posunúť nejakú funkciu označenú tagom alebo názov_funkcie. 
                                            #V našom prípade štvorec ktorý chceme posunúť o 5 doprava,
                                            # takto by vyzeral canvas.move("štvorec",5,0) 
                                                  


def kocečka():                                  #Vytvoril som si len def navyše aby som ti mohol predviesť ako vytvoriť cyklus niečoho
    canvas.create_line(100,100,200,200)
                                            
for i in range(1,1000):                         #Cyklus robíme viacerími spôsobmi, jeden je ten že dáš mu začiatočnú a
                                                # koncovú hodnotu, do kedy ma počítať 
    kocečka()                                   # to je ten --> for i in range():
    canvas.create_line(200,200,300,300)
                                                
#Tento druhý spôsob je u mňa nabiflený a zatiaľ neviem poriadne ako funguje :
def opakovanie():                     #Vytvoríš skupinu funkcií ktorú nazveš opakovanie 
    canvas.after(100,opakovanie)      # --->  canvas.after(čas po ktorom sa spustí skupina funkcií, názov_funkcie) 
                                      #V tomto prípade musíš dať opakovanie aby dookola išla táto funkcia
                                      
    

    canvas.after(100, kocečka)        #Znova canvas.after() tu dávaš už tú samotnú funkciu ktorá 
                                      # má fungovať dookola ktorú si vytvorila

opakovanie()                          #Musíš vyvolať samotné opakovanie ---- ak más def názov_funkcie(): 
                                      # a chceš ho spustiť, musíš ho dať so ().  
x=0                                    
if (x<=10):                                 # if poznáš z minulého roka, stále musíš do zátvorky dať podmienku aby to fungovalo
    canvas.create_oval(100,100,200,200)     
elif(150!=x):                               # elif je vpodstate akokeby další if len s tým že funguje už ako else a to 
    canvas.create_oval(100,100,200,200)     # znamená že nemusíš používať ešte na konci else: 
else:                                       #Je to tzv. ukončenie if, ktoré vykoná funkciu v takej možnosti ktorá 
                                            #nebola tá "správna" v if 
    canvas.create_rectangle(100,300,400,500)
    


button1 = tkinter.Button(text="nakresli kocku", command = kocečka) # tkinter.Button ti vytvorí tlačidlo na plátne (nemusíš davať 
                                                                   # umiestnenie)
                                                                   #Stále musí byť to tlačidlo v nejakej premennej (button1)
                                                                   # ---> tkinter.Button(text= "čo chceš mať napísané v tlačidle", 
                                                                   #      command = spustí nejakú skupinu funkcií (nedávaš zátvorky) )
                                                                   

button1.pack()                                                     #Na spustenie premennej používaš
                                                                   # ---> názov premennej(button1).pack()
                                                                   
entry1 = tkinter.Entry()                                           #Vytvorí okienko/ textové pole do ktorého môžeš niečo písať,
                                                                   # ak chceme využiť informáciu z okienka, 
                                                                   # tak tá je uložená automaticky
                                                                   # vo funkcií --> názov_premennej_okienka {entry1}.get{anglicky dostať}() 
                                                                   #Funkciu budeš mať dalej


entry1.pack()                                                      #Takisto ako keď sme spúštali tlačidlo

canvas.create_text(200,200, text=entry1.get())                     #Tu sme využili informáciu z okienka v 
                                                                   #ktorej si niečo pred spustením napísala
                                                                   #Ak do okienka má sa napísať nejaké číslo ktoré potom využíješ
                                                                   # pri napr. výpčtoch tak celé to entry1.get() dáš do 
                                                                   # int() {integer -> číslo} --> int(entry1.get()) 