# for i in range(10):
#     print(chr(97+i))


    
# chr --> character
# ord --> ordinary


# for i in range(97,107):
#     print(chr(i), end="")
    
priezvisko_str = input("Napíš svoje priezvisko: ")
if  chr(65)<= priezvisko_str[0] <= chr(90) or (chr(192)<= priezvisko_str[0] <= chr(222) and priezvisko_str[0] != 125) or priezvisko_str[0] ==chr(138)or chr(140) <= priezvisko_str[0]<= chr(143) :
    #  "A " <= priezvisko_str[0] <= "Z":
    print("Vieš napísať svoje priezvisko :)")
else: 
    print("Zle si napísal Priezvisko!!")