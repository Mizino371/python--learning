#zápis 10 výšok žiaka pomocou input()
p_ziakov = 10
t_vysky = [0] * p_ziakov
for i in range(p_ziakov):
    t_vysky[i] = int(input(f"Zadaj výšku žiaka č.{i+1}: "))



#zoradenie  
t_vysky.sort()
priemer = sum(t_vysky)/p_ziakov
print("a) Vzostupné usporiadane: ",end=" ")
for i2 in range(p_ziakov): 
    print(t_vysky[i2], end=" ")

#vyrátanie mediánu na základe priemeru dvoch stredných hodnôt
med = (t_vysky[4] + t_vysky[5]) /2
print(f"\nb) Priemer výšky žiakov je: {priemer}")
print(f"c) medián výšky žiakov je: {med}")
