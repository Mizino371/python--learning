vstup = int(input("Zadaj číslo v desiatkovej sústave: "))
zvysok  = ""
sustava = int(input("Zadaj do akej sústavy chceš premeniť číslo: "))
while vstup !=0:
    if sustava == 16:
        if vstup%sustava >=10:
            pismeno = vstup%sustava - 10
            zvysok += chr(65+pismeno)
            vstup = vstup// sustava
        
            
        else:       
            zvysok += str(vstup%sustava)
            vstup = vstup//sustava
    else:
            zvysok += str(vstup%sustava)
            vstup = vstup//sustava
        
    
vystup = ""
for i in range(len(zvysok)):
    vystup += zvysok[-i-1]
    
print(vystup)
