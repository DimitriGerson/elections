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

class TableSqlite :
    """
    Le but de cette classe est la création de table je veux que mon code soit
    suffisamment fort pour pouvoir faire remonter pourquoi cela se passe mal
    et être capable de définir très clairement d'où provient le problème"""
    def __init__(self,requete,nomTable,controleur):
        """
        
        Il me manque les parametres
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
        erreur = 0
        try:
            if type(requete)== str:
                self.requete=requete
                print("1")
            else:
                self.requete = None
                print ("votre requete est nulle.")
                erreur = 1
        except:
            print("problème de requete")
            erreur = 1
        finally:
            try:
                if type(nomTable) == str:
                    self.nomTable=nomTable
                    print("2")
                else:
                    self.nomTable = None
                    print("Votre nom de table est nul.")
                    erreur = erreur +1
            except:
                print("problème de nom de table")
                erreur = erreur +1
            finally:
                try:
                    
                    if str(type(controleur)) == "<class 'tuple'>" :
                        self.controleur=controleur
                        print("3")
                    else:
                        print(type(controleur))
                        self.controleur = None
                        print("Votre controleur est nul.")
                        erreur = erreur + 1
                except:
                    print("problème de controleur")
                    print(type(controleur))
                    erreur = erreur + 1
                finally:
                    print("Fin de d'initialisation de table.")
                    if erreur > 0:
                        del self
                        print("objet détruit ?")
                        
        
    def creationTable(self):
        """
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
        Création de la table Communes
        fin de procédure de création de la table Communes.
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
        finally:   
            print("fin de procédure de création de la table " + self.nomTable + ".")
    
        try:
            self.controleur[1].execute ("SELECT * FROM " + self.nomTable + ";")
        except Exception as e:
            print("Une erreur est survenue lors de la creation de la table : " + self.nomTable )
            print(e)
        finally:
            try :
                if self.controleur[1].fetchone()[0]==1:
                    print("La table " + self.nomTable + " a au moins une ligne.")
            except Exception as e:
                print("La table " + self.nomTable + " est vide !")
                
    def ajoutligneTable(self,baserequete,ajout):
        """faire la doc

        """

        
        self.controleur[1].execute(baserequete,ajout)
        self.controleur[0].commit()

    def interrogeTable(self,requete):
        bob = self.controleur[1].execute(requete)
        
        return bob


#Ce snippet active les doctest et donc mes tests dans Example
if __name__ == "__main__":
    print("Bonjour")
    from doctest import testmod
    testmod()
    print("Les tests de la documentation ont été effectués")
    
