#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    *****************Présentation du projet*****************

    Documentation pour le projet "Analyse des élections"

    *****************Les différents Modules*****************

    1)interface

    2)accès à la base de données

    3)Module HTML

    4)Tests (Ce module est présent dans chacun des trois autre module mais je voudrais créer au final un module de tests)

    ********************************************************
    ********************************************************
    ********************************************************

    Le but de l'ensemble de ces classes est de réaliser une application qui analyse
    les résultats des elections en France en partant dans un premier temps de Rosny-sous-bois
    Ce projet est réalisé en Python 3

    2)accés à la base de données
    Ce module est celui dans le quel vous vous trouvez.
    Dans son ensemble il gère les transactions avec les bases de données.
    Il est composé :
    -d'un module qui est propre à l'application "Analyss des élections" Celle ci contiendra uniquement les données
    -d'un module générale qui a pour vocation d'être réutilisable est totalement indépendante des données.
    Nous cherchons à créer le moins de dépendances possible avec les données pour maximiser la réutilisation du code.
    Nous cherchons aussi a faire de l'écocode en réduisant nos appels aux serveurs en se servant des imports en utilsant from
    pour minimiser nos import.

    Nous utilisons différent types de tests pour notre code le premier niveau étant directement dans le code grace au doctest.
    Ce type de tests sont lancés après modification du fichier ou sur l'ensemble des fichiers ou d'un lot de fichier depuis un
    fichier .bat

    Un deuxième type de test sont fait via des fichiers testunits ceux-ci ne sont pas encore réaliser aujourd'hui.
    
    Ce module gère les accés à la base de données sur SQLite. Il fait donc partie du module générale.
    La bibliothèque présente ici gère les accés à la base de données.
    Elle ne s'occuppe pas d'ecrire de modifier ou d'intéroger la base de données.

    Author Dimitri Gerson
"""

    
from sqlite3 import connect
   
class ControleurBDSqlite(object):
    

    """La classe ControleurBDSqlite permet de se connecter à une base de donnée SQlite
    elle crée la base si celle-ci n'existe pas et établit la connexion pour passer des requetes.
 
    Cette classe crée en deux temps des controleurs pour des bases de données
    en sqlite et cet objet permet d'établir une connexion avec une base de données, de faire des transactions
    et de fermer la connexion.
    Utilisation :
    A la creation de l'objet controleurBDSqlite, il faut donner un nom à la base et le controleur rajoutera le .db
    exemple
    moncontroleur = ControleurBDSqlite("Ma_Base")
    Un fichier Ma_Base.db sera créé
    
    Le parametre est donc le nom de la bdd sans .db.
    Si celle-ci existe déjà rien ne sera modifié.
    Les principales methodes sont :
    -ouvrirConnexion()
    -fermerConnexion()

    """
    
    #initialisation d'un objet.
    def __init__(self,mabase):
        """Cette methode d'initialisation crée le nom de la  base de données
        param mabase: nom de la base
        type mabase: string
        :return:
        :rtype:
        Example:
        >>> mabase = ControleurBDSqlite("base")
        
        .. seealso:: Référence à une autre partie du code
        .. warning:: Avertissement
        .. note:: Note
        .. todo:: Les test Units
        """
        
        self.nom = mabase + ".db"
        
    #ouveture de la connexion.    
    def ouvrirConnexion(self):
        
        """
        La methode ouvrirConnexion() active les clés étrangères et renvoie un tableau de deux éléments
        [0] = connecteur et [1] = curseur
        param :
        type :
        :return conn, curs
        :rtype: tulpe
        Example:
        >>> mabase = ControleurBDSqlite("base")
        >>> bob = mabase.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()

        .. seealso:: Référence à une autre partie du code
        .. warning:: Avertissement
        .. note:: Attention nous avons choisi d'activé les clés étrangères à la connexion
        car SQlite ne le fait pas automatiquement cette dépendance nous semble acceptable.
        .. todo:: Les test Units
        """
        
        try:
            self.conn = connect(self.nom)
            self.curs =self.conn.cursor()
            print("ouverture de la connexion")
            self.curs.execute("PRAGMA foreign_keys = ON")
            print("Clés étrangères activées")
            return(self.conn,self.curs)
            
        except:
            print("Impossible d'ouvrir la connexion")
        finally:
            print("Fin de la methode ouvrirConnexion()")
            
    #Fermeture de la connexion        
    def fermerConnexion(self,connecteur):
        """
        Cette methode permet de fermer la connexion de l'objet
        param :
        type :
        :return 
        :rtype: 
        Example:
        >>> mabase = ControleurBDSqlite("base")
        >>> bob = mabase.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> mabase.fermerConnexion(bob)
        La connexion est fermée
        Fin de la methode fermerConnexion()

        .. seealso:: Référence à une autre partie du code
        .. warning:: Avertissement
        .. note:: Note
        .. todo:: Les test Units
        """
        
        try:
            connecteur[1].close()
            print("La connexion est fermée")
        except:
            print("Nous n'avons pas pu fermer la connexion")
        finally:
            print("Fin de la methode fermerConnexion()")

    #Passage de requete     
    def requete(self,maRequete,tableauConnecteur):
        """pour passer une requête nous avons besoin d'une requete SQL l'objet doit déjà avoir son connecteur et son curseur
        Il faudrait vérifier que curseur et connecteur existent.
        C'est une méthode interne pour qu'un utilisateur passe une requête il doit passer par la méthode sans avoir à écrire du SQL.
        Pour le passage de requete il est conseillé de passer par la classe CreationTable
        pour créer une nouvelle table
        Pour le passage de requete pour la modification de table la classe données sera plus
        appropriée
        Pour le passage de requete pour questionner la base de données une autre classe
        sera créée prochainement
        Cette forme de passage de requete n'est pas sûr car elle est trop permissive et non robuste
        je la garde en dépannage si j'ai besoin de passer une requete très vite.

        Example:
        >>> mabase = ControleurBDSqlite("base")
        >>> bob = mabase.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> mabase.requete(req,bob)
        La requête a été réalisée
        """

        tableauConnecteur[1].execute(maRequete)
        tableauConnecteur[0].commit()
        print("La requête a été réalisée")

       
if __name__ == "__main__":
    print("Bonjour")
    from doctest import testmod
    testmod()
    print("Les tests de la documentation ont été effectués")
    

