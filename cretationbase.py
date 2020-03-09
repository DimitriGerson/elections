#!/usr/bin/python3
# -*- coding: latin-1 -*-
"""
*****************Pr�sentation du projet*****************

Voici une premi�re documentation pour le projet "Analyse des �lections"

*****************Les diff�rents Modules*****************

1)interface

2)acc�s � la base de donn�es

3)Module HTML

4)Tests

********************************************************
********************************************************
********************************************************

Le but de l'ensemble de ces classes est de r�aliser une application qui analyse
les r�sultats des elections en France en partant dans un premier temps de Rosny-sous-bois
Ce projet est r�alis� en Python 3

La biblioth�que pr�sente ici g�re les acc�s � la base de donn�es en �criture et en lecture

2)acc�s � la base de donn�es
Ce module g�re les acc�s � la base de donn�es sur SQLite3

"""
import sqlite3
import creationTable
curs = None
try:
#cr�ation de la connexion � ma base de donn�es


    
    conn =sqlite3.connect("Les_elections.db")

#cr�ation du curseur de pour la base de donn�es
    curs = conn.cursor()
    print("Connexion � la base de donn�es Les_elections.db")
except Exception as e:
    print("!!! Erreur lors de la connexion !!!")
finally:
    print("fin de proc�dure de connexion")   
if curs != None:
    
    print ("Votre connexion fonctionne.")
else:
    print ("!!!! Erreur de Connexion curs a une valeur nulle.")
    print ("L'application va quitter.")
    quit()
    
#activation des cl�s �trang�res
curs.execute("PRAGMA foreign_keys = ON")
print("Cl�s �trang�res activ�es")
    
#cr�ation de la requete pour la table Communes
req = '''CREATE TABLE IF NOT EXISTS Communes(
id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
Code_Postal TEXT);'''
#nom de la table
table = "Communes"
creationTable.creationTable(req,table,curs,conn)

#cr�ation de la table Scrutins
#Pour chaque scrutin une table exemple pr�sidentielle 2017
#cette table devrait etre en 1 � n pour l'ensemble des communes.
#Finalement elle n'a pas de cardinalit�
#ma_ref_Scrutins INTEGER,FOREIGN KEY('ma_ref_Scrutins') REFERENCES Communes('id_Commune')ON DELETE CASCADE

#cr�ation de la requete pour la table Communes
req = '''CREATE TABLE IF NOT EXISTS Scrutins(
id_Scrutin INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
Annee INTEGER
);'''
#nom de la table
table = "Scrutins"
creationTable.creationTable(req,table,curs,conn)

# cette table ne semble pas n�cessaire et est une redite de celle d'au dessus
#Je voulais au d�part faire deux table pour s'il y avait deux fois dans la m�me ann�e un m�me scrutin,
#pour pouvoir l'appeler second scrutin de pr�sidentielle je garde la table au cas o�.
req = '''CREATE TABLE IF NOT EXISTS Type_de_scrutins(
id_Type_de_scrutin INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
ma_ref_Type_de_scrutin INTEGER,
FOREIGN KEY('ma_ref_Type_de_scrutin') REFERENCES Scrutin('id_Scrutin')
ON DELETE CASCADE);'''
#nom de la table
table= "Type_de_scrutins"
creationTable.creationTable(req,table,curs,conn)

#cette table repr�sente le tour d'un scrutin si le scrutin est � deux tour
#il y a deux lignes sinon une.
#Cette table est li�e � la table scrutin.
# il n'hexiste qu'une seul ligne pour chaque tour toute les autres tables font r�f�rence � celle-ci.
req = '''CREATE TABLE IF NOT EXISTS Tours(
id_Tour INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Numero_du_tour INTEGER,
ref_Scrutin INTEGER,
FOREIGN KEY('ref_Scrutin') REFERENCES Scrutins('id_Scrutin')
ON DELETE CASCADE);'''
#nom de la table
table= "Tours"
creationTable.creationTable(req,table,curs,conn)

#--Cette tables et les suivantes sont referenc�es � leur commune et � leur tour pour pouvoir etre identifiees
req = '''CREATE TABLE IF NOT EXISTS Donnees_generales(
id_Donnees_generales INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Inscrits INTEGER,
Abstentions INTEGER,
Votants INTEGER,
Blanc INTEGER,
Nuls INTEGER,
Exprimes INTEGER,
ref_Tour INTEGER,
ref_Commune INTEGER,
FOREIGN KEY('ref_Tour') REFERENCES Tours('id_Tour'),
FOREIGN KEY('ref_Commune') REFERENCES Communes('id_Commune')
ON DELETE CASCADE);'''
#nom de la table
table= "Donnees_generales"
creationTable.creationTable(req,table,curs,conn)

#Cette table repr�sente les partis elle se trouve au-dessus des candidats.
#Elle n'a aucune table au-dessus d'elle.
req = '''CREATE TABLE IF NOT EXISTS Partis(
id_Parti INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
Tendance TEXT);'''
#nom de la table
table= "Partis"
creationTable.creationTable(req,table,curs,conn)

#Les candidats sont li�s � un parti. Ils ont des r�sultat (voir table r�sultat)
#Ici le candidat
req = '''CREATE TABLE IF NOT EXISTS Candidats(
id_Candidat INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
ref_Parti INTEGER,
FOREIGN KEY('ref_Parti') REFERENCES Partis('id_Parti')
ON DELETE CASCADE);'''
#nom de la table
table= "Candidats"
creationTable.creationTable(req,table,curs,conn)

#Ici le r�sultat 
req = '''CREATE TABLE IF NOT EXISTS Resultat_candidats(
id_Resultat_Candidat INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nombre_de_voix INTEGER,
ref_Candidat INTEGER,
ref_Parti INTEGER,
ref_Tour INTEGER,
ref_Commune INTEGER,
FOREIGN KEY('ref_Candidat') REFERENCES Candidats('id_Candidat')
FOREIGN KEY('ref_Parti') REFERENCES Partis('id_Parti'),
FOREIGN KEY('ref_Tour') REFERENCES Tours('id_Tour'),
FOREIGN KEY('ref_Commune') REFERENCES Communes('id_Commune')
ON DELETE CASCADE);'''
#nom de la table
table= "Resultat_candidats"
creationTable.creationTable(req,table,curs,conn)

##Cr�ation de la tables Adjoints
#pour les listes comprenant plusieurs personnes
req = '''CREATE TABLE IF NOT EXISTS Adjoints(
id_Adjoint INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
ref_Candidat INTEGER,
FOREIGN KEY('ref_Candidat') REFERENCES Candidats('id_Candidat')
ON DELETE CASCADE);'''
#nom de la table
table= "Adjoints"
creationTable.creationTable(req,table,curs,conn)
print("Cr�ation de la base de donn�es termin�e :")

"""************************************************************"""
""" Fin de la cr�ation de la base"""


#Maintenant je dois cr�er l'ensemble des requets pour inserer et n'avoir plus qu'� me soucier du contenu.

#creation d'une ligne dans la table Communes

req = ''' INSERT INTO Communes (Nom, Code_Postal) VALUES("Rosny-sous-bois", 93110);'''

curs.execute(req)
conn.commit()

req = '''SELECT id_Commune FROM Communes WHERE Nom = "Rosny-sous-bois"'''
curs.execute(req)
print(curs.fetchone())
req = ''' INSERT INTO Scrutins (Nom, Annee) VALUES ("Pr�sidentielle", 2017);'''

curs.execute(req)
conn.commit()

req = ''' INSERT INTO Tours (Numero_du_tour, ref_Scrutin) VALUES(1,1);'''
curs.execute(req)
conn.commit()

req = '''INSERT INTO Tours (Numero_du_tour, ref_Scrutin) VALUES(2,1);'''
curs.execute(req)
conn.commit()



req = ''' INSERT INTO Donnees_generales(Inscrits, Abstentions, Votants,Blanc, Nuls, Exprimes, ref_Tour, ref_Commune)
   VALUES ( 23232, 6171, 17061, 523, 0, 16538, 1, 1);'''
curs.execute(req)
conn.commit()
req = '''INSERT INTO Partis(Nom, Tendance) VALUES("La France insoumise", "Extreme Gauche");'''
curs.execute(req)
conn.commit()
req = '''INSERT INTO Candidats (Nom, ref_Parti) VALUES ("Jean-Luc MELENCHON",1);'''
curs.execute(req)
conn.commit()
req = ''' INSERT INTO Resultat_Candidats( Nombre_de_voix,ref_Candidat, ref_Parti, ref_Tour, ref_Commune) VALUES(4476, 1,1,1,1);'''
curs.execute(req)
conn.commit()
req = '''INSERT INTO Partis(Nom, Tendance) VALUES(?,?)'''
valeurs = [("La R�publique en marche", "Centre Droite"), ("Les R�publicains", "Droite"), ("Rassemblement National", "Extreme Droite"), ("Parti Socialiste", "Gauche"),("Debout la R�publique","Extreme Droite"), ("Union populaire r�publicaine","Droite"), ("Nouveau Parti Anticapitaliste", "Extreme Gauche"), ("R�sistons", "Centre Droit"), ("Lutte Ouvri�re", "Extreme Gauche"), ("Solidarit� et progr�s", "Centre Droit")]
curs.executemany(req, valeurs)
conn.commit()
req ='''INSERT INTO Candidats (Nom, ref_Parti) VALUES(?,?)'''
valeurs = [("Emmanuel Macron",2),("Fran�ois Fillon",3),("Marine Lepen",4),("Beno�t Hamon",5),("Nicolas Dupont-Aignan",6),("Fran�ois Asselineau",7),("Philippe Poutou",8),("Jean Lassalle",9),("Nathalie Arthaud",10),("Jacques Cheminade",11)]
curs.executemany(req, valeurs)
conn.commit()
req = ''' INSERT INTO Resultat_Candidats (Nombre_de_voix,ref_Candidat, ref_Parti,ref_Tour,ref_Commune)  VALUES (?,?,?,?,?)'''
valeurs =[(4220,2,2,1,1),(2755,3,3,1,1),(2504,4,4,1,1),(1283,5,5,1,1),(678,6,6,1,1),(226,7,7,1,1),(143,8,8,1,1),(115,9,9,1,1),(77,10,10,1,1),(61,11,11,1,1)]
curs.executemany(req, valeurs)
conn.commit()

conn.close()

"""if __name__ == "__main__":
    import doctest
    doctest.testmod()"""
