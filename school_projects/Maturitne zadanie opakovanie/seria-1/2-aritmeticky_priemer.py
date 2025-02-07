p_porodcov = int(input("Zadaj počet porodcov: "))
tb_znamok = [0.0] * p_porodcov
for i in range(p_porodcov):
    vstup = input(f"Známka porodcu číslo {i+1}\n (použi formát 0.0) : ")
    tb_znamok[i] = float(vstup) #zapísanie desatinneho čisla do tabulky po poradí
tb_znamok.sort()
tb_znamok = tb_znamok[1:-1] # ignorácia jedného najvyššieho a najnižšieho hodnotenia
priemer_znamok = sum(tb_znamok)/(p_porodcov-2) #výpočet priemeru (okrem dvoch krajných)

print(f"Výsledná známka je: {priemer_znamok}")