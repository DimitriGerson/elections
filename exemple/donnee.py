#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Ce fichier python contient l'ensemble des requetes SQL pour la création d'une table.
Ces requetes sont rangées dans un tableau"""

""" Ce fichier doit etre lu par un "verificateur_formateur" de requete SQL
Dans ce cas le verificateur verifie que toutes les requetes commence par CREATE TABLE IF NOT EXISTS
 copie le nom de la table verifie que la requete se fini par un ; puis rajoute en
 début et fin les '''"""


#création de la requete pour la table Communes
req1 = '''CREATE TABLE IF NOT EXISTS Communes(
id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
Code_Postal TEXT);'''
#nom de la table
table1 = "Communes"


#création de la requete pour la table Communes
req2 = '''CREATE TABLE IF NOT EXISTS Scrutins(
id_Scrutin INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
Annee INTEGER
);'''
#nom de la table
table2 = "Scrutins"

req3 = '''CREATE TABLE IF NOT EXISTS Type_de_scrutins(
id_Type_de_scrutin INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
ma_ref_Type_de_scrutin INTEGER,
FOREIGN KEY('ma_ref_Type_de_scrutin') REFERENCES Scrutin('id_Scrutin')
ON DELETE CASCADE);'''
#nom de la table
table3= "Type_de_scrutins"

#cette table représente le tour d'un scrutin si le scrutin est à deux tour
#il y a deux lignes sinon une.
#Cette table est liée à la table scrutin.
# il n'hexiste qu'une seul ligne pour chaque tour toute les autres tables font référence à celle-ci.
req4 = '''CREATE TABLE IF NOT EXISTS Tours(
id_Tour INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Numero_du_tour INTEGER,
ref_Scrutin INTEGER,
FOREIGN KEY('ref_Scrutin') REFERENCES Scrutins('id_Scrutin')
ON DELETE CASCADE);'''
#nom de la table
table4= "Tours"

#--Cette tables et les suivantes sont referencées à leur commune et à leur tour pour pouvoir etre identifiees
req5 = '''CREATE TABLE IF NOT EXISTS Donnees_generales(
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
table5= "Donnees_generales"

#Cette table représente les partis elle se trouve au-dessus des candidats.
#Elle n'a aucune table au-dessus d'elle.
req6 = '''CREATE TABLE IF NOT EXISTS Partis(
id_Parti INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
Tendance TEXT);'''
#nom de la table
table6= "Partis"

#Les candidats sont liés à un parti. Ils ont des résultat (voir table résultat)
#Ici le candidat
req7 = '''CREATE TABLE IF NOT EXISTS Candidats(
id_Candidat INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
ref_Parti INTEGER,
FOREIGN KEY('ref_Parti') REFERENCES Partis('id_Parti')
ON DELETE CASCADE);'''
#nom de la table
table7= "Candidats"

req8 = '''CREATE TABLE IF NOT EXISTS Resultat_candidats(
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
table8= "Resultat_candidats"

##Création de la tables Adjoints
#pour les listes comprenant plusieurs personnes
req9 = '''CREATE TABLE IF NOT EXISTS Adjoints(
id_Adjoint INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
ref_Candidat INTEGER,
FOREIGN KEY('ref_Candidat') REFERENCES Candidats('id_Candidat')
ON DELETE CASCADE);'''
#nom de la table
table9= "Adjoints"

monTableau=[(req1,table1),(req2,table2),(req3,table3),(req4,table4),
            (req5,table5),(req6,table6),(req7,table7),
            (req8,table8),(req9,table9)]

base = "base_de_donnees_elections"    
