subor = open('4.roč/zimne-prazdniny/mesta1.txt', 'r')
for riadok in subor:
    polozky = riadok.strip().split(';')  # Split and remove trailing spaces
    print(polozky)
