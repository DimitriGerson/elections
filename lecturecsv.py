import csv, sqlite3

with open('ville_93.csv','r',encoding='utf8') as don:
    dr = csv.reader(don)
    Communes_93=[]
    for i in dr:
        print(i)
        b=[]
        b.append(i[0])
        b.append(i[1])
        Communes_93.append(b)     
print(Communes_93)

mon_fichier = open("Communes_93.txt", "w") # Argh j'ai tout écrasé !
mon_fichier.write(str(Communes_93))
mon_fichier.close()

