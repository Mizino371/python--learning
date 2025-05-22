subor = open("krstne_mena.txt", "r")
mena_ch = {}
mena_d = {}
# [ch,d]
for riadok in subor:
    riadok = riadok.strip().split(" ")
    if riadok[0] == "ch":
        if riadok[1] not in mena_ch:
            mena_ch[riadok[1]] = 1
        else:
            mena_ch[riadok[1]] += 1
    else:
        if riadok[1] not in mena_d:
            mena_d[riadok[1]] = 1
        else:
            mena_d[riadok[1]] += 1

print(mena_ch)
print(mena_d)
max_d = [1, ""]
max_ch = [1, ""]

for m_ch in mena_ch:
    print(f"Meno {m_ch} sa vyskytlo {mena_ch[m_ch]}krát")
    if max_ch[0] < mena_ch[m_ch]:
        max_ch[0] = mena_ch[m_ch]
        max_ch[1] = m_ch
for m_d in mena_d:
    print(f"Meno {m_d} sa vyskytlo {mena_d[m_d]}krát")
    if max_d[0] < mena_d[m_d]:
        max_d[0] = mena_d[m_d]
        max_d[1] = m_d
print(f"Najčastejšie vyskytujúce sa chlapčenské meno je: {max_ch[1]}")
print(f"Najčastejšie vyskytujúce sa dievčenské meno je:{max_d[1]}")
