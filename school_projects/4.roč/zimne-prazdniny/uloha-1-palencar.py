# V textovom súbore mesta1.txt sú hlavné mestá Európy. 
# Na každom riadku je nazov mesta, bodkočiarka a názov krajiny. 
# Vytvorte program, ktory vyzve používatela, aby zadal hlavné mestá
# Europy, kdore navstivil. Program porovná zoznam navštívených miest s mestami, 
# ktore sú v súbore, a pouivatelovi napíšee, ktoré mestá este nenavstivil. 
# Textovy súbor môžeme v programe prečitat len raz. Ukátka suboru:

subor = open("4.roč/zimne-prazdniny/mesta1.txt","r")

vstup = input("Zadaj hlavné mestá ktoré si navšívil (oddeľ ich čiarkou ("",""))")
zoznam_plus_miest = [mesto.strip().upper() for mesto in vstup.split(",")]
riadok = subor.readline()
n_mesto = 1
while riadok !="":
    mesto_stat= riadok.strip().split(";")
    riadok = subor.readline()
    if mesto_stat[0].upper() not in zoznam_plus_miest:
        print(f"{n_mesto}. Nenavšívil si ešte {mesto_stat[0]} v štáte {mesto_stat[1]}")
        n_mesto+=1
       

subor.close()


