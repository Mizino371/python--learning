# 1000 hodov kockou 
# výpis 1 padla ....x krát
# 2...
#-||- 
#-||-
#-||-
#6....
import random as r

kocka = [0]*6

for i in range(1000):
    hod = r.randint(1,6)
    kocka[hod-1]+=1
    
    
for i in range(6):  
    print(f"strana s číslom {i+1}: {kocka[i]}")