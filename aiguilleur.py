#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Controleur de la base de données
#Son role est de créer une base données et de s'y connecter
#l'utilisateur donne le nom de sa base et le controleur établit la
#connexion avec la base de donnée
from ControleursBases import ControleurBDSqlite as BD
import sqlite3

import csv

#Controleur de la création de table
#Son role est de créer les tables
from CreationTable import TableSqlite as TS

#Les donnees sont dans ce fichier
#Deux données le nom de la base et les requetes de création
from donnee import monTableau, base, table_nom

from requete import req_ins_Com, req_sel_Com 
#pour la creation de la base



#pour ajouter des données à la table Communes
Table_Com="Communes"
with open('ville_93.csv','r',encoding='utf8') as don:
    dr = csv.reader(don)
    Communes_93=[]
    for i in dr:
        print(i)
        b=[]
        b.append(i[1])
        b.append(i[0])
        b = tuple(b)
        
        #b.append(table_nom[0])
        Communes_93.append(b)     
print(Communes_93)
#attention je dois créer ma requete avec les deux premier elemente de Communes_93         
     
        #for ee in tb:
            #print(ee)
            #tuple(ee).append(table_nom[0])
            
            #tb.append(ee)
            



"""Ce fichier a pour role d'aiguiller les données pour créer une base de données
"""
leControleur = BD(base)
connexion = leControleur.ouvrirConnexion()
# je dois deplacer cette fonction dans Creationtable Je dois changer
# le nom de creation
for ele in monTableau:
    maTable = TS(ele[0],ele[1],connexion)
    maTable.creationTable()
leControleur.fermerConnexion(connexion)

#leControleur = BD(BASE)
connexion = leControleur.ouvrirConnexion()

#insertion des données dans la table commune

for ele in Communes_93:
    bob= (req_ins_Com , ele)
    
    
    bob = str(bob)
    bob = bob[1:-1]
    print(type(bob))#dans ce cas bob ne peut être un string mais un string + un tulpe
    print(bob)
    maTable = TS(bob,Table_Com,connexion)
    maTable.ajoutligneTable(req_ins_Com, ele)
    
leControleur.fermerConnexion(connexion)

connexion = leControleur.ouvrirConnexion()
maTable = TS("SELECT * FROM Communes",Table_Com,connexion)
bob2= maTable.creationTable()
leControleur.fermerConnexion(connexion)
connexion = leControleur.ouvrirConnexion()
maTable = TS(bob,Table_Com,connexion)
requeteici = maTable.interrogeTable(req_sel_Com)
a=requeteici.fetchone()
print(a[0])
#il faut entrer à la main l'ensemble des données qui vont me permettre de rentrer les autres en series
#ces données sont les scrutins et les tours
#les partis
#les candidats
