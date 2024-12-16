znamky = input("Zadaj svije známky: ")

n = len(znamky)
Prospel = True
neprospel = False
scitane_znamky = 0
for i in range(n):
    if int( znamky[i]) == 5 :
        neprospel = True
        print("Neprospel")
        break
        
    elif int( znamky[i]) ==3:
        Prospel = False
    
    scitane_znamky += int( znamky[i])

priemer = scitane_znamky/n

if priemer <= 1.5 and Prospel and not neprospel :
    print("Prospel s vyznamenaním")
elif (priemer<=2 and Prospel == False) or 1.5 <priemer<=2 and not neprospel :
    print("Prospel veľmi dobre")
elif 2< priemer <= 4 and neprospel ==False :
    print("Prospel")

print(f"Tvoj priemer je: {round(priemer,2)}")
            
        