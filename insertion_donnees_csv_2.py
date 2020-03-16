import csv, sqlite3
from requete import req_ins_Com,req_ins_DG,req_ins_RC

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

"""
:todo:rajouter les données manquantes les references dans les bases de données
pour cela je dois me connecter à la base de données et récupérer les différents paramètres
"""
with open('Aubervilliers.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    #dr = csv.DictReader(fin) # comma is default delimiter
    dr = csv.reader(fin)
    print(dr)
    #to_db = [(i['col1'], i['col2']) for i in dr]
    DG=[] #tableau des données générales
    TableDG=0
    TableRC=0
    a=0
    tableau_requetes=[]
    for i in dr:
        a=a+1
        print(a)
        print(i)
        print(i[0])
        if a==2:
            table='Commune'
            req=(req_ins_Com,i,table)
            #je dois plutôt récupérer id_Commune en intérogeant la base
            #pour la replacer dans les différentes table
            tableau_requetes.append(req)
        elif a==3:
            tableRC=i[0]
        elif a==4:
            req=(req_ins_RC,i,tableRC)
            #il faut transformer le nom du candidat en ref au candidat
            #il faut trouver la reference au parti
            #il faut trouver la reference au tour
            #il faut trouver la reference à la commune
            tableau_requetes.append(req)
        elif a==5: 
            req=(req_ins_RC,i,tableRC)
            #il faut transformer le nom du candidat en ref au candidat
            #il faut trouver la reference au parti
            #il faut trouver la reference au tour
            #il faut trouver la reference à la commune
            tableau_requetes.append(req)
        elif a==6:
            tableDG=i[0]
        elif a==7:
            DG.append(i[1])
        elif a==8:
            DG.append(i[1])
        elif a==9:
            DG.append(i[1])
        elif a==10:
            DG.append(i[1])
        elif a==11:
            DG.append(i[1])
        elif a==12:
            DG.append(i[1])
        elif a==13:
            DG.append(i[0])
        elif a==14:
            DG.append(i[0])
            req=(req_ins_DG,DG,tableDG)
            tableau_requetes.append(req)
            print("fin du second tour")
        elif a==15:
            pass#j'ai déjà le Table
        elif a==16:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==17:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==18:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==19:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==20:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==21:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==22:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==23:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==24:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==25:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==26:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==27:
            pass
        elif a==28:
            DG=[]
            DG.append(i[1])
        elif a==29:
            DG.append(i[1])
        elif a==30:
            DG.append(i[1])
        elif a==31:
            DG.append(i[1])
        elif a==32:
            DG.append(i[1])
        elif a==33:
            DG.append(i[1])
        elif a==34:
            DG.append(i[0])
        elif a==35:
            DG.append(i[0])
            req=(req_ins_DG,DG,tableDG)
            tableau_requetes.append(req)
            print("fin du premier tour")
            
            
            
            
            
    for ele in tableau_requetes:
        print("Un element")
        print (ele)
        for o in ele:
            
            print(o)
#ecriture dans un fichier qui portera le nom de la commune
mon_fichier = open("Aubervillier.txt", "w") # Argh j'ai tout écrasé !
mon_fichier.write(str(tableau_requetes))
mon_fichier.close()

mon_fichier = open("Aubervillier.txt", "r")
contenu = mon_fichier.read()
print('impression du contenu')
print(contenu)
mon_fichier.close()


#cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
#con.commit()
#con.close()
