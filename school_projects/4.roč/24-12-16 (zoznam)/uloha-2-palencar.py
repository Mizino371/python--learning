import random as r 
cislice = 10*[0] #[0,0,0,0,...]

for i in range(100):
    r_cifra = r.randint(0,9)
    cislice[r_cifra] +=1
    
for i2 in range(10):
    print(f"Priemerný výskyt číslice {i2} je {cislice[i2]}%")