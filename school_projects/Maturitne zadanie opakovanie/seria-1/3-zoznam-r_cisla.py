import random as r 
l_num = [0] * 10
for i in range(100): #nahodne generovanie čísel a následne zvvyšovanie počtu výskytu čísla n 
    r_num = r.randrange(10)
    l_num[r_num] += 1
    
for i in range(10):
    print(f"Percento výskytu čísla {i} je: {round((l_num[i]/100)*100,2) }%")