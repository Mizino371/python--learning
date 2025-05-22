vstup = input("Zadaj URL adresu s / na konci: ")
vstup = vstup.strip()
protokol = vstup[:vstup.index("://")]
print(protokol)
domena  = vstup[vstup.index("://")+3:]
print(domena)

subdomena = domena[:domena.index("/")]
najvyssia_domena  = [ i for i in range(len(domena)) if domena[-i] == "."]
print(najvyssia_domena)
print(subdomena)