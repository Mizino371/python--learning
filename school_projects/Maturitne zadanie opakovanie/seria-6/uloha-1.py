vstup = input("Napíš gramatické cvičenie ktoré je gramaticky správne: ")
for i in range(50):
    print("/\n")

sprava_veta = vstup.strip()
gram_cvicenie = vstup.replace("y","*").replace("ý","*").replace("Y","*").replace("Ý","*").replace("i","*").replace("í","*").replace("I","*").replace("Í","*")
print(gram_cvicenie)
na_kontrolu = input("Napíš gramatické cvičenie ktoré je gramaticky správne: ")
na_kontrolu = na_kontrolu.strip()
skontrolovana_veta = ""
p_chyb =0
for i in range(len(na_kontrolu)):
    if na_kontrolu[i] == sprava_veta[i]:
        skontrolovana_veta += na_kontrolu[i]
        continue
    else:
        skontrolovana_veta += "!"
        p_chyb += 1

print(skontrolovana_veta)
print(f"Mal si {p_chyb} chýb")