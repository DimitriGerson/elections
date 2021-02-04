#!/usr/bin/python3
# -*- coding: utf-8 -*-
#import sqlite3 je pense que je n'ai pas besoin d'importer sqlite
from csv import reader

#Controleur bdd :role est de créer une base données et de s'y connecter
#l'utilisateur donne le nom de sa base et le controleur établit la
#connexion avec la base de donnée
from ControleursBases import ControleurBDSqlite as BD
#Controleur de la création de table. Son role est de créer les tables
from CreationTable import TableSqlite as TS

#Les donnees sont dans ce fichier
#Deux données le nom de la base et les requetes de création
from donnee import monTableau, base, table_nom
from requete import req_ins_Com #, req_sel_Com 

#pour ajouter des données à la table Communes depuis un fichier csv
#Table_Com=monTableau[0][1] #pour avoir le nom de la table communes
#faire une fonction à qui l'on donne le nom de la base le fichier csv et le nom
#de la table la fonction en déduit la requete dans mon tableau et fait l'ajout
def ajoutDonneesCsvDansTable(maBase,maTable,fichierCsv):

    leControleur = BD(maBase)
    connexion = leControleur.ouvrirConnexion()
    monIndex=None
    for ele in monTableau :
        a=0
        if ele[1] == maTable:
            
            monIndex=monTableau.index(ele)
    maTable = TS(monTableau[monIndex][0],monTableau[monIndex][1],connexion)#pour la connexion à la base et à la table que l'on souhaite je peux déplacer la connexion de la base endehors de la boucle
    with open(fichierCsv,'r',encoding='utf8') as don:
        dr = reader(don)
        for ele in dr: #ici on va chercher dans le fichier csv les communes ligne par ligne
            lesDonnees=(ele[1],ele[0]) #on inverse les données pour qu'elle correspondent à ce que l'on veut d'abord le nom puis le code postale. 
            maTable.ajoutligneTable(req_ins_Com, lesDonnees) #création de la requete + insertion dans la base de données grace à l'objet de classe TableSqlite
    
    leControleur.fermerConnexion(connexion)

ajoutDonneesCsvDansTable(base,'Communes','communes-francaises_2016.csv')
