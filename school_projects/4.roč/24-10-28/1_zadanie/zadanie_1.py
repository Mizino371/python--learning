subor = open("24-10-28/1_zadanie/mala abeceda.txt", "w")
for i in range(97,122):
    subor.write(str(i)+" "+chr(i)+"\n")
subor.close()
    