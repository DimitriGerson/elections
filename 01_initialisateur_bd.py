
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
"""
def bddCreation(nomDeLaBase,tableauRequeteNomTable):
    """Cette fonction crée la base de données avec ces tables
    on  pourrait en faire une classe"""
    leControleur = BD(nomDeLaBase)
    connexion = leControleur.ouvrirConnexion()
    # je dois deplacer cette fonction dans Creationtable Je dois changer
    # le nom de creation
    for ele in tableauRequeteNomTable:
        maTable = TS(ele[0],ele[1],connexion)
        maTable.creationTable()
    leControleur.fermerConnexion(connexion)

bddCreation(base,monTableau)
