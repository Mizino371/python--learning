subor1= open("4.roč/24-11-18/vstup.txt","r")
subor2 = open("4.roč/24-11-18/vystup.txt","w")
#madam = konktrola preho a posledneho 
# 0 <=> -1
# 1 <=> -2
# 2 <=> -3

# y1 = x+1
# y2 = -x +1 
def ide_o_palindrom():
    for riadok in subor1:
        palindrom = riadok.strip()

        dlzka_slova = len(palindrom) -1
        vysledok = True
        kladne_x = 0

        while dlzka_slova > kladne_x and vysledok:
            if palindrom[kladne_x] == palindrom[dlzka_slova]:
                vysledok = True
                
            else:
                vysledok = False
                subor2.write(f"{palindrom} - nie je palindróm\n")
            
            kladne_x += 1
            dlzka_slova -= 1
            
        if vysledok :
            subor2.write(f"{palindrom} - ide o palindróm\n")

ide_o_palindrom() 
subor1.close() 
subor2.close()