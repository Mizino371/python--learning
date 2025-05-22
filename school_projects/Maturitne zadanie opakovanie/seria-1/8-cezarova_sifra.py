
veta = input("Zadaj vetu ktorú chceš zašifrovať \n(posun bude náhodne vygenerovaný): ")
import random as r 
n= r.randint(5,50) #náhodný posun písmen
veta = veta.strip()
pismenka = [0]*len(veta) 
print(f"Posun písmen je { n}")
print(chr(126))

for i in range(len(veta)):
    pismenka[i] = ord(veta[i]) #zmena každého znaku na ascii kod a zaradenie do samostatných prvkov listu
    if pismenka[i] != 32:
        if (pismenka[i]+n) >=126: #krajná situácia = prechod za index a začatie od začiatku 
            pismenka[i] = 33+(pismenka[i]+n-126)
        else:
            pismenka[i]+=n
    print(chr(pismenka[i]),end="") # postupné ukladanie písmenok za sebou  
   

