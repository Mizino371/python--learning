dlhy_riadok =open("dlhyriadok.txt","r")
vystupny = open("dlhyriadok_vystup.txt","w")

dlzka_riadka = int(input("Zadaj dlzku riadka: "))
riadok = dlhy_riadok.readline()
riadok = riadok.strip()
for i in range((len(riadok))//dlzka_riadka):
    vystupny.write(riadok[ (i * dlzka_riadka) : (i * dlzka_riadka) + dlzka_riadka ] + "\n")

dlhy_riadok.close()
vystupny.close()