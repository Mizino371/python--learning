subor = open("4.roč/24-11-14/slova.txt","r")
n = 0
riadok = subor.readline()
while riadok != "STOP\n":
    n += 1
    riadok = subor.readline()
print(f"{n}")