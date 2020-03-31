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
class InterrogeTable:
    """Cette classe est la classe mère de TableSqlite elle contient
    les methodes suivantes :
    -ajoutLigneTable
    -ajoutLigneSansCommit
    -faireCommit
    -interrogeTable
    """

    def __init__(self,controleur):
        """
        param : controleur
        type : 'ControleursBases'
        :return
        :rtype: 'InterrogeTable'
        
        Example:
        >>> import ControleursBases
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>>
        """
        
        
        try:        
            if str(type(controleur)) == "<class 'tuple'>" :
                self.controleur=controleur
                print("1")
            else:
                print(type(controleur))
                self.controleur = None
                print("Votre controleur est nul.")
                del self
                print("objet détruit.")
        except:
            print("problème de controleur")
            print(type(controleur))
            del self
            print("objet détruit.")
        else:
            print("L'initialitation de la table est réalisée.")
        finally:
            print("Fin de d'initialisation de table.")

    def ajoutLigneTable(self,baserequete,ajout):
        """faire la doc
            la base de la requete est : 'INSERT INTO Resultat_candidats(Nombre_de_voix,ref_Candidat,ref_Parti,ref_Tour,ref_Commune) VALUES(?,?,?,?,?);'
            l'ajout est un tuple : (126, 4, 4, 1, 1127)
        param : baserequete
        type : str
        param : ajout
        type : tuple
        :return
        :rtype:
        Example:
        >>> import ControleursBases
        >>> import CreationTable
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = CreationTable.TableSqlite(req,table,tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        1
        2
        table réalisée.
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes est vide !
        >>> uneTable = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>> requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        >>> monTuple = ('Paris',75000)
        >>> uneTable.ajoutLigneTable(requete,monTuple)
        La requête s'est déroulée normalement.
        >>> controleur.fermerConnexion(tableau)
        La connexion est fermée
        Aucune erreur !
        Fin de la methode fermerConnexion()
        """
        #il faudrait que l'ajout de ligne se charge aussi de la connexion dans le cas où
        #il n'y a pas de connexion. c'est assez fragile en fait ici.
        try:
            self.controleur[1].execute(baserequete,ajout)
            self.controleur[0].commit()
        except Exception as e:
            print("Une erreur est survenue lors de l'ajout de la ligne.")
            print (e)
        else:
            print("La requête s'est déroulée normalement.")

    def ajoutLigneSansCommit(self,baserequete,ajout):
        """
        param : baserequete
        type : str
        param : ajout
        type : tuple
        :return
        :rtype:
        Example:
        >>> import ControleursBases
        >>> import CreationTable
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = CreationTable.TableSqlite(req,table,tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        1
        2
        table réalisée.
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes est vide !
        >>> uneTable = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>> requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        >>> monTuple = ('Marseille',13000)
        >>> uneTable.ajoutLigneSansCommit(requete,monTuple)
        La requête s'est déroulée normalement.
        """
        
        try:
            self.controleur[1].execute(baserequete,ajout)
        except Exception as e:
            print("Une erreur est survenue lors de l'ajout de la ligne.")
            print (e)
        else:
            print("La requête s'est déroulée normalement.")
        
    def faireCommit(self):
        """
        Example:
        >>> import ControleursBases
        >>> import CreationTable
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = CreationTable.TableSqlite(req,table,tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        1
        2
        table réalisée.
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes a au moins une ligne.
        >>> uneTable = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>> requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        >>> monTuple = ('Marseille',13000)
        >>> uneTable.ajoutLigneSansCommit(requete,monTuple)
        La requête s'est déroulée normalement.
        >>> uneTable.faireCommit()
        Commit réalisé.
        """
        
        try:
            self.controleur[0].commit()
        except Exception as e:
            print("Une erreur est survenue lors de la consultation de la bdd.")
            print (e)
        else:
            print('Commit réalisé.')
            
    def interrogeTable(self,requete):
        """Attention cette requete peut être potentiellement dangereuse si la requete passée n'est
        pas une interrogation de base.
        Rien n'empêche à ce niveau de passer une requete d'insertion.
        Example
        >>> import sqlite3
        >>> import ControleursBases
        >>> import CreationTable
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = CreationTable.TableSqlite(req,table,tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        1
        2
        table réalisée.
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes a au moins une ligne.
        >>> uneTable = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>> requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        >>> monTuple = ('Marseille',13000)
        >>> uneTable.ajoutLigneSansCommit(requete,monTuple)
        La requête s'est déroulée normalement.
        >>> uneTable.faireCommit()
        Commit réalisé.
        >>> uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Marseille';''').fetchone()
        La requête s'est déroulée normalement.
        (2,)
        """
        if str(requete[0:6])=='SELECT':
            try:
                bob = self.controleur[1].execute(requete)
            except Exception as e:
                print("Une erreur est survenue lors de la consultation de la bdd.")
                print (e)
            else:
                print ("La requête s'est déroulée normalement.")
                return bob
            bob = None
            return bob
        else:
            print('Votre requete ne commence pas par "SELECT".')
            print(str(requete[0:6]))


#Ce snippet active les doctest et donc mes tests dans Example
if __name__ == "__main__":
    print("Bonjour")
    from doctest import testmod
    testmod()
    print("Les tests de la documentation ont été effectués")
