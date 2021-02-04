#!/usr/bin/python3
# -*- coding: utf-8 -*-

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


DONNEES=monTableau
BASE=base

"""Ce fichier a pour role d'aiguiller les données pour créer une base de données
"""
leControleur = BD(BASE)
connexion = leControleur.ouvrirConnexion()
for ele in DONNEES:
    maTable = TS(ele[0],ele[1],connexion)
leControleur.fermerConnexion()
