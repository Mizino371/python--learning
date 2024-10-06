veta = input("Napíš vetu: ")

# Babka ide domov. 
# Babka ide d*m*v.
vystup = ""
for i in range(len(veta)):
    if veta[i] == "y" or  veta[i] == "Y" or veta[i] == "I" or veta[i] == "i":
        vystup = vystup + "*"
    else:
        vystup = vystup + veta[i]
print(vystup)
    
# Diana ide do šmyku