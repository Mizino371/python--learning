print("zadaj dva rovnako dlhé mená")
# name1 = input("Zadaj prvé meno: ")
# name2 = input("zadaj druhé meno: ")
name1 = "miso"
name2 = "Peto"
vystup = ""
if len(name1) !=len(name2):
    print("error")
    
else: 
    for i in range(len(name2)):
        vystup= vystup + name1[i] + name2[i]
print(vystup)

