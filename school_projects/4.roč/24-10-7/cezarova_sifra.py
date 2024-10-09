
def cezarova_sifra():
    
    vstupna_veta = input("zadaj slovo: ")
    krok_sifrovania = int(input("krok šifrovania: "))
    
    slovo_sifrovane  =""
    
    for i in range(len(vstupna_veta)):
        
        # velke pismena
        if 65<=ord(vstupna_veta[i] ) <=90:
            if ord(vstupna_veta[i]) + krok_sifrovania > 90:
                slovo_sifrovane = ord("A")+  (ord(vstupna_veta[i]) + krok_sifrovania -1) -(ord("Z"))
            else:
                slovo_sifrovane = ord(vstupna_veta[i])+krok_sifrovania
        
        # male pismena
        elif 97 <=ord(vstupna_veta[i] )<= 122:
            if ord(vstupna_veta[i] )+krok_sifrovania > 122:
                slovo_sifrovane = ord("a") +(ord(vstupna_veta[i]) + krok_sifrovania -1) -  ord("z")
            else:
                slovo_sifrovane = ord(vstupna_veta[i])+krok_sifrovania
                
        
        print(chr(slovo_sifrovane),end="")
        
    # znova =input("Chceš zašifrovať dalšie slovo? (Ano/Nie)")
    # znova = znova.lower()
    # if znova == "ano" or znova == "nie" or znova == "n" or znova == "a":
    #     cezarova_sifra()

cezarova_sifra()