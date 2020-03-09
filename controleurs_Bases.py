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
Ce projet est r�alis� en Python 3.8

La biblioth�que pr�sente ici g�re les acc�s � la base de donn�es en �criture et en lecture

2)acc�s � la base de donn�es
Ce module g�re les acc�s � la base de donn�es sur SQLite3

"""
import sqlite3

"""Ce fichier contient les controleurs de la base de donnees
je vais modifiier ces fonction pour en faire des objets"""
    
class ControleurBDSqlite(object):
    
    """Cette classe cr�e des objets controleur pour des bases de donn�es
    en sqlite et c'est objets permettent d'interagir avec une base de donn�e.
    Il faut donner un nom � la base et le controleur rajoutera le .db
    Le parametre est le nom de la bdd sans .db"""

    """initialisation avec cr�ation de la base et de la connection et du curseur
    cette m�thode return un tulpe"""
    def __init__(self,mabase):
        """Cette methode d'initialisation cr�e le nom de la  base de donn�es"""
        self.nom = mabase + ".db"
        
    def ouvrirConnexion(self):
        """ouvrir Connexion cr�e un connecteur et son curseur.
        self.conn pour le connecteur
        self.curs pour le curseur"""
        
        try:
            self.conn =sqlite3.connect(self.nom)
            self.curs =self.conn.cursor()
            print("ouverture de la connexion")
            self.curs.execute("PRAGMA foreign_keys = ON")
            print("Cl�s �trang�res activ�es")
            return(self.conn,self.curs)
            
        except:
            print("Impossible d'ouvrir la connexion")
        finally:
            print("Fin de la methode ouvrirConnexion()")
            
    def fermerConnexion(self):
        "Cette methode permet de fermer la connexion de l'objet"
        try:
            self.conn.close()
            print("La connexion est ferm�e")
        except:
            print("Nous n'avons pas pu fermer la connexion")
        finally:
            print("Fin de la methode fermerConnexion()")

#Passage de requete     
    def requete(self,maRequete):
        """pour passer une requ�te nous avons besoin d'une requete SQL l'objet doit d�j� avoir son connecteur et son curseur
        Il faudrait v�rifier que curseur et connecteur existent.
        C'est une m�thode interne pour qu'un utilisateur passe une requ�te il doit passer par la m�thode sans avoir � �crire du SQL."""
        #try:
        self.curs.execute(maRequete)
        self.conn.commit()
        print("La requ�te a �t� r�alis�e")
        #except:
         #   print("Une erreur est survenue nous ne pouvons r�aliser votre requ�te")
        #finally:
          #  print("Fin de la requ�te.")
    
                  

    
#faire un cr�ateur de table
    
    def creationTable(self):
        """Cette m�thode cr�e une table en paussant des questions � l'utilisateur
        C'est un mod�le na�f � modifier"""
        self.table="CREATE TABLE IF NOT EXISTS "
        self.nomTable=input("Bonjour vous allez cr�er une table, quel est son nom ?")
        self.id_Table="id_" + self.nomTable
        self.table_2 = " (" + self.id_Table + " INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE"
        self.nombre_de_colonne = input("Combien de colonne souhaitez-vous ?")
        self.nombre_de_colonne = int(self.nombre_de_colonne)
        if self.nombre_de_colonne > 1:
            """Self.i parce que nos tables on au moins 1 colonne avec une cl� primaire.
            C'est un choix de conception."""
            self.i=2
            while self.nombre_de_colonne>0:
                
                self.nom_colonne = input("Quel nom pour la colonne " + str(self.i) + " ?")
                self.type_de_variable = input("Quel type de variable ?")
                self.nombre_de_colonne= self.nombre_de_colonne - 1
                self.i=self.i+1
        #pour finaliser les requete il me suffit de rajouter le type de variable et leur nom a concaqu�n�er
                self.table_2 = self.table_2 + ', ' + self.nom_colonne + ' ' +self.type_de_variable  
        
        self.table_fin = ");"
        self.table_finale = self.table + " " + self.nomTable + " " + self.table_2 + self.table_fin
        print(self.table_finale)
        self.question = input("Validez-vous la table ?(oui/non):")
        if self.question == "oui" :
            self.creationTable = input("souhaitez-vous cr�er la table " + self.nomTable + " ?(oui/non):")
            if self.creationTable == "oui" :
                bob=ControleurBDSqlite("unautrebase")
                bob.requete(self.table_finale)
                #self.matable.requete(self.table_finale)
    #Ajouter des donn�es � une table
    def ajoutDeDonneesTable(self):
        """Cette m�thode ajoute des donn�es � une table dans la base de donn�es"""

#fonction de connection
# Cette fonction permet de me connecter � la base mabase et rajoute l'extention .db au fichier
# Elle renvoie le curseur et la connection pour s'en servir il faut cr�er une variable �gale � la fonction. ex element de connexion= connection("unebase")

def connection(mabase):
    mabase = mabase + ".db"
    conn = sqlite3.connect(mabase)
    curs = conn.cursor()
    return (curs, conn )
#fonction de requete
def requete(connecteur, maRequete):
    connecteur[0].execute(maRequete)
    connecteur[1].commit()
#creation d'une base de donn�es en exemple
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
#creation de la base de donn�e via un controleur
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

