vstup = input("Vyučujúci zadá vetu: ")
print_veta = str(vstup)
spravna_veta = vstup
for i in range(len(print_veta)):
    pismeno = str(print_veta[i-1])
    if pismeno == "y" or pismeno == "ý" or pismeno == "Y" or pismeno == "i" or pismeno == "í" or pismeno == "l" or pismeno == "ĺ":
        print_veta =print_veta[:i-1]+"!"+print_veta[i:]
print(print_veta)
v_na_kontrolu = input("Žiak zadá vetu: ")

p_chyb = 0
for i in range(len(spravna_veta)):
    if v_na_kontrolu[i] == spravna_veta[i]:
        continue
    else:
        p_chyb +=1

print(f"Mal si {p_chyb} chýb")