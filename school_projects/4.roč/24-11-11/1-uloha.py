subor1 = open("4.roč/24-11-11/prihlaseni.txt","r")
subor2 = open("4.roč/24-11-11/prihlaseni-mena.txt","w")

cislo_riadku = 0
for riadok in subor1:
    if cislo_riadku % 2 == 0:
        #subor1.readline()
        subor2.write(riadok)
    cislo_riadku += 1

    
subor1.close()
subor2.close()