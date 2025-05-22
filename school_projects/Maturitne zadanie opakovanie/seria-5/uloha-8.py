subor = open("/Users/m1promichalpalencar/Desktop/python--learning/school_projects/Maturitne zadanie opakovanie/seria-5/nakup.txt", "r")
zoz_cien = []

for riadok in subor:
    riadok = float(riadok.strip())
    zoz_cien.append(riadok)
if len(zoz_cien) < 3:
    print("Nedostatok druhov tovaru na zľavu")
zoz_cien = sorted(zoz_cien)

print(f"Nákup bez zľavy je {sum(zoz_cien)}€")
print(f"Zľava 5% sa uplatní na položku s cenou {zoz_cien[-1]}€")
vysl_suma = sum(zoz_cien[:-1]) + (zoz_cien[-1] * 0.95)
print(f"Výsledná cena je {vysl_suma:.2}€")
subor.close()