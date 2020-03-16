from requete import selectWhereSqlite,req_ins_Scru,req_ins_Partis,req_ins_Cand,req_ins_Tours

from donnee import monTableau, base, table_nom
import sqlite3

import csv

#Controleur de la création de table
#Son role est de créer les tables
from CreationTable import TableSqlite as TS
from ControleursBases import ControleurBDSqlite as BD


tableauScrutin=[('Presidentielles','2017')]

#insertion dans la base de données
leControleur = BD(base)
connexion = leControleur.ouvrirConnexion()
maTable = TS(monTableau[1][0],monTableau[1][1],connexion)

maTable.ajoutligneTable(req_ins_Scru, tableauScrutin[0])


requete=selectWhereSqlite('id_Scrutin','Scrutins', 'nom', 'Presidentielles','AND', 'Annee', '2017')
maTable = TS(monTableau[1][0],monTableau[1][1],connexion)
print (requete)
ref_election=maTable.interrogeTable(requete)
a=ref_election.fetchone()
a=a[0]
print(a)
tableauTours=[('1',a),('2',a)]
leControleur.fermerConnexion(connexion)
connexion = leControleur.ouvrirConnexion()
maTable = TS(monTableau[3][0],monTableau[3][1],connexion)
#insertion dans la base de données
for e in tableauTours:
    print(e)
    maTable.ajoutligneTable(req_ins_Tours, e)
    
leControleur.fermerConnexion(connexion)




tableauPartis=[("La France insoumise", "Extreme Gauche"),("La République en marche", "Centre Droite"), ("Les Républicains", "Droite"), ("Rassemblement National", "Extreme Droite"), ("Parti Socialiste", "Gauche"),("Debout la République","Extreme Droite"), ("Union populaire républicaine","Droite"), ("Nouveau Parti Anticapitaliste", "Extreme Gauche"), ("Résistons", "Centre Droit"), ("Lutte Ouvrière", "Extreme Gauche"), ("Solidarité et progrés", "Centre Droit")]
#insertion dans la base de données
connexion = leControleur.ouvrirConnexion()
maTable = TS(monTableau[5][0],monTableau[5][1],connexion)
for ele in tableauPartis:
    print(ele)
    maTable.ajoutligneTable(req_ins_Partis, ele)

leControleur.fermerConnexion(connexion)
tableauCandidat = [("Jean-Luc MELENCHON",1),("Emmanuel Macron",2),("François Fillon",3),("Marine Lepen",4),("Benoît Hamon",5),("Nicolas Dupont-Aignan",6),("François Asselineau",7),("Philippe Poutou",8),("Jean Lassalle",9),("Nathalie Arthaud",10),("Jacques Cheminade",11)]    
tablCT=[]
bob=[]
#je veux entrer le nom et le partis et la requete me renvoie le nom et la ref_Partis
requete= selectWhereSqlite("*",monTableau[5][1],WHERE=" ")
leControleur = BD(base)
connexion = leControleur.ouvrirConnexion()
maTable = TS(monTableau[5][0],monTableau[5][1],connexion)
print (requete)
ref_Partis=maTable.interrogeTable(requete)
a=ref_Partis.fetchall()
for ele in a:
        print (ele[0])
        for elem in tableauCandidat:
            if ele[0] == elem[1]:
                bob.append(elem[0])
                bob.append(ele[1])
                ba=tuple(bob)
                tablCT.append(ba)
                bob=[]

print(tablCT)
                
leControleur.fermerConnexion(connexion)

connexion = leControleur.ouvrirConnexion()
maTable = TS(monTableau[6][0],monTableau[6][1],connexion)
for ele in tableauCandidat:
    print(ele)
    maTable.ajoutligneTable(req_ins_Cand, ele)
leControleur.fermerConnexion(connexion)
#[nom,ref_parti]="clause select avec 1 parametre Nom", Nom
#tableauCandidats[(Nom,ref_Parti)]
