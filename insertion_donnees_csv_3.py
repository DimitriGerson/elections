print("dimitri")
import csv, sqlite3
from requete import req_ins_Com,req_ins_DG,req_ins_RC,selectWhereSqlite
from donnee import monTableau, table_nom
print("loulou")
from remplir_base import rechercheIdTableDansListe, table_donnees
print("popo")
#pour avoir le préfixe id_
carid="id_"
table='Candidats'
#con = sqlite3.connect(":memory:")
#cur = con.cursor()
#cur.execute("CREATE TABLE t (col1, col2);") # use your column names here
print("Dimitri")
"""
:todo:rajouter les données manquantes les references dans les bases de données
pour cela je dois me connecter à la base de données et récupérer les différents paramètres
"""
#ref au scrutin
table_Scru=table_nom[1]

req_Ins=req_ins_RC #pour changer la requete pour l'insersion venir ici
table_Ins = table_nom[7] #pour changer la table d'insersion venir ici
table_Cand= table_nom[6]
table_Com= table_nom[0]
table_Tour =table_nom[3]
#table_donnees =['Communes', [(1, 'Saint-Denis', '93200'), (2, 'Montreuil', '93100'), (3, 'Aulnay-sous-Bois', '93600'), (4, 'Aubervilliers', '93300'), (5, 'Drancy', '93700'), (6, 'Noisy-le-Grand', '93160'), (7, 'Épinay-sur-Seine', '93800'), (8, 'Pantin', '93500'), (9, 'Bondy', '93140'), (10, 'LeBlanc-Mesnil', '93150'), (11, 'Sevran', '93270'), (12, 'Saint-Ouen', '93400'), (13, 'Bobigny', '93000'), (14, 'Livry-Gargan', '93190'), (15, 'Rosny-sous-Bois', '93110'), (16, 'Noisy-le-Sec', '93130'), (17, 'Gagny', '93220'), (18, 'LaCourneuve', '93120'), (19, 'Villepinte', '93420'), (20, 'Stains', '93240'), (21, 'Bagnolet', '93170'), (22, 'Tremblay-en-France', '93290'), (23, 'Neuilly-sur-Marne', '93330'), (24, 'Clichy-sous-Bois', '93390'), (25, 'Villemomble', '93250'), (26, 'Pierrefitte-sur-Seine', '93380'), (27, 'Montfermeil', '93370'), (28, 'Romainville', '93230'), (29, 'LesLilas', '93260'), (30, 'LesPavillons-sous-Bois', '93320'), (31, 'Neuilly-Plaisance', '93360'), (32, 'LePré-Saint-Gervais', '93310'), (33, 'LeBourget', '93350'), (34, 'LeRaincy', '93340'), (35, 'Villetaneuse', '93430'), (36, 'Dugny', '93440'), (37, "L'Île-Saint-Denis", '93450'), (38, 'Vaujours', '93410'), (39, 'Gournay-sur-Marne', '93460'), (40, 'Coubron', '93470')], 'Scrutins', [(1, 'Presidentielles', 2017), (2, 'Presidentielles', 2017), (3, 'Presidentielles', 2017), (4, 'Presidentielles', 2017)], 'Type_de_scrutins', [], 'Tours', [(1, 1, 1), (2, 2, 1)], 'Donnees_generales', [], 'Partis', [(1, 'La France insoumise', 'Extreme Gauche'), (2, 'La République en marche', 'Centre Droite'), (3, 'Les Républicains', 'Droite'), (4, 'Rassemblement National', 'Extreme Droite'), (5, 'Parti Socialiste', 'Gauche'), (6, 'Debout la République', 'Extreme Droite'), (7, 'Union populaire républicaine', 'Droite'), (8, 'Nouveau Parti Anticapitaliste', 'Extreme Gauche'), (9, 'Résistons', 'Centre Droit'), (10, 'Lutte Ouvrière', 'Extreme Gauche'), (11, 'Solidarité et progrés', 'Centre Droit'), (12, 'La France insoumise', 'Extreme Gauche'), (13, 'La République en marche', 'Centre Droite'), (14, 'Les Républicains', 'Droite'), (15, 'Rassemblement National', 'Extreme Droite'), (16, 'Parti Socialiste', 'Gauche'), (17, 'Debout la République', 'Extreme Droite'), (18, 'Union populaire républicaine', 'Droite'), (19, 'Nouveau Parti Anticapitaliste', 'Extreme Gauche'), (20, 'Résistons', 'Centre Droit'), (21, 'Lutte Ouvrière', 'Extreme Gauche'), (22, 'Solidarité et progrés', 'Centre Droit'), (23, 'La France insoumise', 'Extreme Gauche'), (24, 'La République en marche', 'Centre Droite'), (25, 'Les Républicains', 'Droite'), (26, 'Rassemblement National', 'Extreme Droite'), (27, 'Parti Socialiste', 'Gauche'), (28, 'Debout la République', 'Extreme Droite'), (29, 'Union populaire républicaine', 'Droite'), (30, 'Nouveau Parti Anticapitaliste', 'Extreme Gauche'), (31, 'Résistons', 'Centre Droit'), (32, 'Lutte Ouvrière', 'Extreme Gauche'), (33, 'Solidarité et progrés', 'Centre Droit')], 'Candidats', [(1, 'Jean-Luc MELENCHON', 1), (2, 'Emmanuel Macron', 2), (3, 'François Fillon', 3), (4, 'Marine Lepen', 4), (5, 'Benoît Hamon', 5), (6, 'Nicolas Dupont-Aignan', 6), (7, 'François Asselineau', 7), (8, 'Philippe Poutou', 8), (9, 'Jean Lassalle', 9), (10, 'Nathalie Arthaud', 10), (11, 'Jacques Cheminade', 11), (12, 'Jean-Luc MELENCHON', 1), (13, 'Emmanuel Macron', 2), (14, 'François Fillon', 3), (15, 'Marine Lepen', 4), (16, 'Benoît Hamon', 5), (17, 'Nicolas Dupont-Aignan', 6), (18, 'François Asselineau', 7), (19, 'Philippe Poutou', 8), (20, 'Jean Lassalle', 9), (21, 'Nathalie Arthaud', 10), (22, 'Jacques Cheminade', 11), (23, 'Jean-Luc MELENCHON', 1), (24, 'Emmanuel Macron', 2), (25, 'François Fillon', 3), (26, 'Marine Lepen', 4), (27, 'Benoît Hamon', 5), (28, 'Nicolas Dupont-Aignan', 6), (29, 'François Asselineau', 7), (30, 'Philippe Poutou', 8), (31, 'Jean Lassalle', 9), (32, 'Nathalie Arthaud', 10), (33, 'Jacques Cheminade', 11)], 'Resultat_candidats', [], 'Adjoints', []]
#Cette table est ficitve pour l'instant je la récupèrerai depuis ma base de donnée

table_Scru=table_nom[1]
print(table_Scru)
id_scru=rechercheIdTableDansListe(table_donnees,table_Scru,"Presidentielles", valeur_2=2017)
print("toto!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(table_donnees)
print(table_donnees[table_donnees.index(table_Scru)+1])

print(id_scru)
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
        if a==1:
            #com=i[0]
            #com_id ="id_" + com[0:-1]
            pass
        
        
        #print(bob[0])
        if a==2:
            table=i[0]#ici j'ai le nom de la commune
            com_id =rechercheIdTableDansListe(table_donnees,table_Com,i[0])
            print(com_id)
            
            #idcommune = carid + bob[0]
            
            
            #req=selectWhereSqlite(com_id,com,"Nom",table)
            #je ne vais pas faire de requête à la base je vais me servir du tableau que j'ai créér important la ma table sqlite
            #je veux l'id de la commune
            
            #tableau_requetes.append(req)#je dois lancer les requetes en même temps
        elif a==3:
            #pourquoi j'ai besoin de resultat_candidats c'est le nom de la table
            pass
        elif a==4:
            #cette succession de commandes fonctionne pour récupérer des données depuis la bdd via un tableau table_donnees pour aller chercher des données dans un csv
            #pour les ordonner pour créer des requêtes.
            #il faudra peut-être rajouter une étape pour que cela soit compréhensible
            #les requetes seront ensuite transmises à la bdd pour insérées ces nouvelles données à leurs tours dans la base de données.
            #il faut que j'ordonne cette succession de commande pour en faire au moins une fonction au mieux une classe
            tour=2
            print(i)
            
            list_sec=i[1:2]#les deux premier elements de la liste je n'ai besoin que du nombre de voix
            #list_sec.reverse() #inverstion
            print(i[0])
            ref_Can=rechercheIdTableDansListe(table_donnees,table_Cand,i[0])
            ref_Parti=rechercheIdTableDansListe(table_donnees,table_Cand,i[0],changeColonne=2)#trouver la reférence du parti je peux via le nom trouver directement la référence au parti
            print("octave")
            print(table_Tour,id_scru,tour)
            ref_Tour=rechercheIdTableDansListe(table_donnees,table_Tour,tour,valeur_2=id_scru)#pour avoir la ref au tour

            print(list_sec)
            list_sec.append(ref_Can)
            list_sec.append(ref_Parti)
            #list_sec.append(id_scru)
            list_sec.append(ref_Tour)
            list_sec.append(com_id)
            print(list_sec)
            
            #il faut transformer le nom du candidat en ref au candidat
            #il faut trouver la reference au parti
            #il faut trouver la reference au tour
            #il faut trouver la reference à la commune
            req=(req_Ins,list_sec,table_Ins)
            print(req)
            caca
            tableau_requetes.append(req)
        elif a==5: 
            req=(req_ins_RC,i,tableIns)
            liste_sec=[]
            #ajouter les resultat en premier
            liste_sec.append(i[1])
            #grace au nom trouver id du candidat
            idCandidat=rechercheIdTableDansListe(table_donnee,table,i[0])
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
