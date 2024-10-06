# import random as r

# for i in range(8):
#     output= ""
#     if i <3 :
#         random_char = chr(r.randint(65,90))
#         output += random_char
     
#     elif i <= 4:
#         random_char = chr(r.randint(48,57))
#         output +=random_char

#     else:
#         random_char = chr(r.randint(97,122))
#         output +=random_char
#     print(output, end="")

import random as r
output= ""
for i in range(8):

    heslo = chr(r.randint(97,122))
    output += heslo
print(output)

nahoda_pozicia_pismena = r.randrange(8)
pismeno_zmena_int = ord(output[nahoda_pozicia_pismena]) -32
nove_velke_pismeno = chr(pismeno_zmena_int)
output = output[:nahoda_pozicia_pismena]+ nove_velke_pismeno+ output[nahoda_pozicia_pismena+1:]
print(output)
    # output += chr(r.randint(65,90))



       
