Keď sme si vytvorili obrázok z viacerých objektov, 
posúva sa ťažšie naraz celý obrázok. 
Museli by sme poznať číslo pvého nakresleného objektu tohto obrázku
a počet nakreslených častí. 
Za predpokladu, že sme ich kreslili hneď v poradí za sebou,
môžeme takýto obrázok posúvať for cyklom od prvého čísla objektu až 
po číslo podľa počtu častí. Je tu však aj jednoduchšia možnosť. 
Všetky časti obrázku si môžeme označiť nejakou spoločnou značkou a potom môžeme 
posúvať objekty, ktoré majú spoločnú značku. 
Objekt si označkujeme pri vytváraní parametrom tags, 
napríklad canvas.create_oval(x,y,x+10,y+10, tags='auto').
Potom môžeme pri posúvaní namiesto čísla objektu použiť jeho značku. 
Napríklad canvas.move('auto', 5, 0) značku môžeme použiť aj pri mazaní objektu. 
V nasledujúcom programe sme nakreslili auto a bicykel a jednotlivé časti týchto 
obrázkov sme si označkovali. Potom ich pomocou časovača posúvame každý zvlášť.
Napíšte program s 2 objektami (bicykel a auto) a nechajte ich zmiznúť z obrazovky 
ako na videu:
