vstup = input("Zadaj svoje známyk na vysvedčení a oddeľ medzerou: ")
vstup = vstup.strip().split(" ")
if vstup.count("5") >0: #rýchla dedukcia na základe známky 5 
    print("Neprospel")
for i in range(len(vstup)): # premena známok z stringu na int
    vstup[i] = int(vstup[i])

priemer = sum(vstup)/len(vstup)

if (priemer <= 1.5) and (3 not in vstup) and (4 not in vstup): #priemer a hľadanie zvyšních neprajných čísel v liste
    print(f"Priemer = {round(priemer,2)} - prospel s vyznamenaním")
elif 1.5<priemer<=2:
    print(f"Priemer = {round(priemer,2)} - prospel veľmi dobre")
elif priemer >2:
    print(f"Priemer = {round(priemer,2)} - prospel")