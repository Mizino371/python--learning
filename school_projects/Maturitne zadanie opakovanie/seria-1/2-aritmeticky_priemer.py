p_porotcov = int(input("Zadaj počet porodcov: ")) #vymaž
tb_znamok = [0.0] * p_porotcov
for i in range(p_porotcov): #použi while
    vstup = input(f"Známka porodcu číslo {i+1}\n (použi formát 0.0) : ")
    tb_znamok[i] = float(vstup) #zapísanie desatinneho čisla do tabulky po poradí
tb_znamok.sort()
tb_znamok = tb_znamok[1:-1] # ignorácia jedného najvyššieho a najnižšieho hodnotenia
priemer_znamok = sum(tb_znamok)/(p_porotcov - 2) #výpočet priemeru (okrem dvoch krajných)

print(f"Výsledná známka je: {priemer_znamok}")