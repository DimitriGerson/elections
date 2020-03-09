#!/usr/bin/python3
# -*- coding: latin-1 -*-
"""
*****************Présentation du projet*****************

Voici une première documentation pour le projet "Analyse des élections"

*****************Les différents Modules*****************

1)interface

2)accès à la base de données

3)Module HTML

4)Tests

********************************************************
********************************************************
********************************************************

Le but de l'ensemble de ces classes est de réaliser une application qui analyse
les résultats des elections en France en partant dans un premier temps de Rosny-sous-bois
Ce projet est réalisé en Python 3.8

La bibliothèque présente ici gère les accés à la base de données en écriture et en lecture

2)accés à la base de données
Ce module gère les accés à la base de données sur SQLite3

"""
import sqlite3

"""Ce fichier contient les controleurs de la base de donnees
je vais modifiier ces fonction pour en faire des objets"""
    
class ControleurBDSqlite(object):
    
    """Cette classe crée des objets controleur pour des bases de données
    en sqlite et c'est objets permettent d'interagir avec une base de donnée.
    Il faut donner un nom à la base et le controleur rajoutera le .db
    Le parametre est le nom de la bdd sans .db"""

    """initialisation avec création de la base et de la connection et du curseur
    cette méthode return un tulpe"""
    def __init__(self,mabase):
        """Cette methode d'initialisation crée le nom de la  base de données"""
        self.nom = mabase + ".db"
        
    def ouvrirConnexion(self):
        """ouvrir Connexion crée un connecteur et son curseur.
        self.conn pour le connecteur
        self.curs pour le curseur"""
        
        try:
            self.conn =sqlite3.connect(self.nom)
            self.curs =self.conn.cursor()
            print("ouverture de la connexion")
            self.curs.execute("PRAGMA foreign_keys = ON")
            print("Clés étrangères activées")
            return(self.conn,self.curs)
            
        except:
            print("Impossible d'ouvrir la connexion")
        finally:
            print("Fin de la methode ouvrirConnexion()")
            
    def fermerConnexion(self):
        "Cette methode permet de fermer la connexion de l'objet"
        try:
            self.conn.close()
            print("La connexion est fermée")
        except:
            print("Nous n'avons pas pu fermer la connexion")
        finally:
            print("Fin de la methode fermerConnexion()")

#Passage de requete     
    def requete(self,maRequete):
        """pour passer une requête nous avons besoin d'une requete SQL l'objet doit déjà avoir son connecteur et son curseur
        Il faudrait vérifier que curseur et connecteur existent.
        C'est une méthode interne pour qu'un utilisateur passe une requête il doit passer par la méthode sans avoir à écrire du SQL."""
        #try:
        self.curs.execute(maRequete)
        self.conn.commit()
        print("La requête a été réalisée")
        #except:
         #   print("Une erreur est survenue nous ne pouvons réaliser votre requête")
        #finally:
          #  print("Fin de la requête.")
    
                  

    
#faire un créateur de table
    
    def creationTable(self):
        """Cette méthode crée une table en paussant des questions à l'utilisateur
        C'est un modèle naïf à modifier"""
        self.table="CREATE TABLE IF NOT EXISTS "
        self.nomTable=input("Bonjour vous allez créer une table, quel est son nom ?")
        self.id_Table="id_" + self.nomTable
        self.table_2 = " (" + self.id_Table + " INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE"
        self.nombre_de_colonne = input("Combien de colonne souhaitez-vous ?")
        self.nombre_de_colonne = int(self.nombre_de_colonne)
        if self.nombre_de_colonne > 1:
            """Self.i parce que nos tables on au moins 1 colonne avec une clé primaire.
            C'est un choix de conception."""
            self.i=2
            while self.nombre_de_colonne>0:
                
                self.nom_colonne = input("Quel nom pour la colonne " + str(self.i) + " ?")
                self.type_de_variable = input("Quel type de variable ?")
                self.nombre_de_colonne= self.nombre_de_colonne - 1
                self.i=self.i+1
        #pour finaliser les requete il me suffit de rajouter le type de variable et leur nom a concaquénéer
                self.table_2 = self.table_2 + ', ' + self.nom_colonne + ' ' +self.type_de_variable  
        
        self.table_fin = ");"
        self.table_finale = self.table + " " + self.nomTable + " " + self.table_2 + self.table_fin
        print(self.table_finale)
        self.question = input("Validez-vous la table ?(oui/non):")
        if self.question == "oui" :
            self.creationTable = input("souhaitez-vous créer la table " + self.nomTable + " ?(oui/non):")
            if self.creationTable == "oui" :
                bob=ControleurBDSqlite("unautrebase")
                bob.requete(self.table_finale)
                #self.matable.requete(self.table_finale)
    #Ajouter des données à une table
    def ajoutDeDonneesTable(self):
        """Cette méthode ajoute des données à une table dans la base de données"""

#fonction de connection
# Cette fonction permet de me connecter à la base mabase et rajoute l'extention .db au fichier
# Elle renvoie le curseur et la connection pour s'en servir il faut créer une variable égale à la fonction. ex element de connexion= connection("unebase")

def connection(mabase):
    mabase = mabase + ".db"
    conn = sqlite3.connect(mabase)
    curs = conn.cursor()
    return (curs, conn )
#fonction de requete
def requete(connecteur, maRequete):
    connecteur[0].execute(maRequete)
    connecteur[1].commit()
#creation d'une base de données en exemple
if __name__ == "__main__":
    #je peux faire un mode plus interactif mais je le ferai endehors de la fonction main. dans une autre fichier python dans une vue

    vraiBase = "bob"
    monconnecteur = connection(vraiBase)
    print (monconnecteur)
    req = '''CREATE TABLE IF NOT EXISTS Communes(
    id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    Nom TEXT,
    Code_Postal TEXT);'''

#requete sous forme de fonction
    requete(monconnecteur, req)
    #fermer cette connexion
#en mode objet
    unebase = "Titi"
    print("Essais en mode objet")
#creation de la base de donnée via un controleur
    nouveau =ControleurBDSqlite(unebase)
    print(nouveau.curs)
    nouveau.requete(req)
    nouveau.fermerConnexion()
    nouveau.ouvrirConnexion()
    nouveau.creationTable()
    #pour selectionner toutes les tables
    
    bob1 = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    #maintenant il faut les montrer
    nouveau.requete(bob1)
    #nouveau.ouvrirConnexion()
    print(nouveau.curs.fetchone())
    nouveau.fermerConnexion()

