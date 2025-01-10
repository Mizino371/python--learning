subor_mesta_a_krajina = open("4.roč/zimne-prazdniny/mesta1.txt", "r")
subor_krajiny = open("4.roč/zimne-prazdniny/krajiny-palencar.txt", "w")

zoznam_krajin = []
for riadok in subor_mesta_a_krajina:
    krajina = riadok.strip().split(";")
    zoznam_krajin.append(krajina[1])

zoznam_krajin = list(set(zoznam_krajin))  # Remove duplicates
zoznam_krajin.sort()

for krajina in zoznam_krajin:
    subor_krajiny.write(krajina + "\n")



subor_mesta_a_krajina.close()
subor_krajiny.close()