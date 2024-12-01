#vyžiada čislo a vypíše jeho celociferný súčet
while True:
    v_cislo = input("Zadaj rôzne celé číslo:")
    cif_sucet = 0
    počet_cif = len(v_cislo)
    for i in range(počet_cif):
        n_cifra = (int(v_cislo)//10**i)%10
        cif_sucet += n_cifra

    print(f"Ciferný súčet čísla: {v_cislo}. je {cif_sucet}")
