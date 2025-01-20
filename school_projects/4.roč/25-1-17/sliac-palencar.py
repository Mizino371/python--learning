s_sliac = open("4.roč/25-1-17/sliac.txt","r")

vstup = input("Zadaj 1 typ počasia ktorý hľadáš: \nJasno = JJ \nPolojasno = PJ\nPolooblačno = PO\nOblačno = OO\n")
vstup = vstup.strip().upper()
skratky_pocasia = {
    "JJ" : ["Jasno",0,0,-100],  #cely nazov, kolko dní, nízka teplota, vysoká teplota
    "PJ" : ["Polojasno",0,0,-100],
    "PO" : ["Polooblačno",0,0,-100],
    "OO" : ["Oblačno",0,0,-100]  
                    }
teplota_pocasie = {}
        
for i in range(1,32):
    riadok = s_sliac.readline().strip().split(" ")
    teplota_pocasie[i] = [int(riadok[0]),skratky_pocasia[riadok[1]][0]]                    
    skratky_pocasia[riadok[1]][1]+=1
    # najnižšía teplota
    if skratky_pocasia[riadok[1]][2] > int(riadok[0]) :
        skratky_pocasia[riadok[1]][2] = int(riadok[0])
    # najvyššia teplota
    if skratky_pocasia[riadok[1]][3] < int(riadok[0]) :
        skratky_pocasia[riadok[1]][3] = int(riadok[0])
 
print(f"Počasie: {skratky_pocasia[vstup][0]}\nPočet dní výskytu je: {skratky_pocasia[vstup][1]}\nNajnižšia teplota: {skratky_pocasia[vstup][2]}\nNajvyššia teplota: {skratky_pocasia[vstup][3]}")