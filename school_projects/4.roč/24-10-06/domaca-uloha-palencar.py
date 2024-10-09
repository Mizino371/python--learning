def opakovanie_scitania():

    scitanec_1 =  int(input("Zadaj prvého sčítanca: "))
    scitanec_2 = int(input("Zadaj druhého sčítanca: "))
    input_vysledok = int(input(f"{scitanec_1} + {scitanec_2} = "))

    spravny_vysledok = scitanec_1 + scitanec_2 

    if (scitanec_1 + scitanec_2) == input_vysledok:
        print("SPRÁVNE ")

    else:
        print(f"NESPRÁVNE . Správny výsledok : {spravny_vysledok}")
    
    hrat_znova = input("Chceš skúsiť znova? (1/0) ")
    if int(hrat_znova) == 1:
        opakovanie_scitania()

        
opakovanie_scitania()