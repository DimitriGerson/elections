
#Controleur de la base de données
#Son role est de créer une base données et de s'y connecter
#l'utilisateur donne le nom de sa base et le controleur établit la
#connexion avec la base de donnée
from ControleursBases import ControleurBDSqlite as BD

#Controleur de la création de table
#Son role est de créer les tables
from CreationTable import TableSqlite as TS

#Les donnees sont dans ce fichier
#Deux données le nom de la base et les requetes de création
from donnee import monTableau, base

#todo les test units
#pour la creation de la base
"""Cette fonction crée une base de données du nom inséré dans base dans le fichier donnee
Pour Créer une base il faut un fichier donnee qui contient les données de création de """

class BaseDeDonnees:
    def __init__(self,nomDeLaBase,tableauRequeteNomTable): 
        """Cette fonction crée la base de données avec ces tables
        on  pourrait en faire une classe"""
        self.nom=nomDeLaBase
        self.tableauCreationBase=tableauRequeteNomTable
        self.leControleur = BD(self.nom)

    def ouvrirCon(self):
        self.connexion = self.leControleur.ouvrirConnexion()
            

    def creationBDD(self):
        self.ouvrirCon()
        for ele in self.tableauCreationBase:
            self.maTable = TS(ele[0],ele[1],self.connexion)
            self.maTable.creationTable()
        self.leControleur.fermerConnexion(self.connexion)
        

mabase = BaseDeDonnees(base,monTableau)
mabase.creationBDD()
