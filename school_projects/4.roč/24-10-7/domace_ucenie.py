
samohlasky = "iíyýIÍYÝ"

veta = input("Zadaj vetu: ")
spravna_veta = veta
for znak in samohlasky:
    veta= veta.replace(znak,"*")

def check_veta():
    skontrolovana_veta = ""
    for i in range(len(veta)):
        if user_in_veta[i] == spravna_veta[i]:
            skontrolovana_veta += user_in_veta[i]
        else:
            skontrolovana_veta += "(!"+spravna_veta[i]+ "!)"
    
    print(skontrolovana_veta)    

print(veta)

user_in_veta = input("Napíš svoju vetu: ")
check_veta()


