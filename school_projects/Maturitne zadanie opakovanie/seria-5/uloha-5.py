subor = open("/Users/m1promichalpalencar/Desktop/python--learning/school_projects/Maturitne zadanie opakovanie/seria-5/vstup.txt","r")
vystup = open("/Users/m1promichalpalencar/Desktop/python--learning/school_projects/Maturitne zadanie opakovanie/seria-5/vystup.txt","w")

for riadok in subor:
def palindrom(text):

    palindrom = True
    text = text.strip()
    for i in range(len(text)//2):
        if text[i] == text[-(i+1)]:
            palindrom = False
            break
    return palindrom

subor.close()
vystup.close()


#použi return