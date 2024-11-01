import random as r

subor = open("24-10-28/2_zadanie/heslo malej abecedy.txt","a")
pocet_hesiel = int(input("Zadaj koľko chceš hesiel: "))
for i in range(pocet_hesiel):
    heslo = ""
    for i2 in range(8):
        random_char =chr(r.randint(97, 122))
        heslo += random_char
    print(heslo,file=subor)
    