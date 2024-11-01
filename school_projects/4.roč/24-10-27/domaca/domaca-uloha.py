# Chceme vytvoriť textový súbor, ktorý obsahuje očíslované riadky postupne číslami 1, 2 až 9. 
# Ktorý z programov je správnym riešením? Nájdite chyby v ostatných programoch.

# # 1
# subor = open('pokus1.txt', 'w')
# for i in range(1, 10):
#     subor.write(i) #–––>chyba (i) je iniger, do zátvoriek môže íst len STRING plus chýba ukončenie riadku "\n"
# subor.close()


#Oprava 1
def oprava(pokus):
    cislo_pokusu = pokus
    subor = open("pokus"+str(cislo_pokusu)+".txt","w")
    for i in range(1, 10):
        subor.write(str(i)+"\n") 
    subor.close()
oprava(1)
# #2
# subor = open('pokus2.txt', 'w')
# for i in range(1, 10):
#     subor.write(i+"\n") # takisto ako v prvej nieje String ale intiger zadefinované v (i)
# subor.close()

#Oprava 2 
oprava(2)

#3 Najmenej náročná možnosť na vykonanie
subor = open('pokus3.txt', 'w')
for i in range(1, 10):                              #SPRÁVNE
    subor.write(str(i)+'\n')
subor.close()

#4 Trochu náročnejšia než možnost 3
subor = open('pokus4.txt', 'w')
for i in range(1, 10):                              #SPRÁVNE
    subor.write(str(i))
    subor.write('\n')
subor.close()

#5 súbor sa stále otvára odznova aj zatvára a za každým opakovaním sa program spustí znova a prepíše prvý riadok 
# for i in range(1, 10):
#     subor = open('pokus5.txt', 'w')
#     subor.write(str(i)+'\n')
#     subor.close()
oprava(5)

print(i,file=subor)
