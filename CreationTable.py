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
from sqlite3 import OperationalError
from ControleursTables import InterrogeTable
class TableSqlite(InterrogeTable):
    """
    Le but de cette classe est la création des tables dans une base de données
    existante. Je veux aussi pouvoir consulter la base de données.
    je veux que mon code soit suffisamment robuste pour pouvoir faire remonter
    pourquoi cela se passe mal et être capable de définir très clairement d'où
    provient le problème.
    Je vais peut-être changer le nom du fichier en GestionTables.py"""
    def __init__(self,requete,nomTable,controleur):
        """
        L'initiatilation de la table se fait avec une requete, le nom de la table
        et un controleur. L'initialisation ne crée pas la table elle prépare la
        création de la table
        le seul parametre important est le controleur, nous avons besoin de requête
        et nom de table que dans le cas où nous créons une table dans le but de ce
        connecter à la base il nous suffit d'un mabase = TableSqlite(controleur)
        
        param : requete
        type : 'str'
        param : nomTable
        type : 'str'
        param : controleur
        type : 'ControleursBases'
        :return
        :rtype: 'TableSqlite'
        
        Example:
        >>> import ControleursBases
        >>> import CreationTable
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
        2
        3
        Fin de d'initialisation de table.
        """
        super().__init__(controleur)#pour initialiser comme la classe mère
        erreur = 0
        try:
            if type(requete)== str:
                self.requete=requete
                print("1")
            else:
                self.requete = None
                print ("votre requete est nulle.")
                del self
                print("objet détruit.")
        except:
            print("problème de requete")
            del self
            print("objet détruit.")
        else:
            try:
                if type(nomTable) == str:
                    self.nomTable=nomTable
                    print("2")
                else:
                    self.nomTable = None
                    print("Votre nom de table est nul.")
                    del self
                    print("objet détruit.")
            except:
                print("problème de nom de table")
                del self
                print("objet détruit.")
            else:
                print("table réalisée.")
            finally:
                    print("Fin de d'initialisation de table.")
                    
                        
                        
        
    def creationTable(self):
        """Cette methode crée la table dans la base de données son nom est
        creationTable attention a ne pasle confondre avec la classe Création
        de table. utilisation objetCreationTable.creationTable()
        param : 
        :return
        :rtype:
        Example:
        >>> import ControleursBases
        >>> import CreationTable
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
        2
        3
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes est vide !
        
        """

        
        try:
            print(self.requete)
            self.controleur[1].execute(self.requete)
            self.controleur[0].commit()
            print("Création de la table " + self.nomTable)
        except OperationalError:
            print("Erreur la table " + self.nomTable + " n'a pas été trouvée")
        except Exception as e:
            print("!!! Une erreur s'est produite lors de la création de la table " + self.nomTable + ".")
            print(e)
        else:
            print("Aucune erreur !")
        finally:   
            print("fin de procédure de création de la table " + self.nomTable + ".")
    
        try:
            self.controleur[1].execute ("SELECT * FROM " + self.nomTable + ";")
        except Exception as e:
            print("Une erreur est survenue lors de la creation de la table : " + self.nomTable )
            print(e)
        else:
            print("Aucune erreur lors de la création de la table !")
        finally:
            try :
                if self.controleur[1].fetchone()[0]==1:
                    print("La table " + self.nomTable + " a au moins une ligne.")
            except Exception as e:
                print("La table " + self.nomTable + " est vide !")
            #il faut fermer la connexion.   

#Ce snippet active les doctest et donc mes tests dans Example
if __name__ == "__main__":
    print("Bonjour")
    from doctest import testmod
    testmod()
    print("Les tests de la documentation ont été effectués")
    
