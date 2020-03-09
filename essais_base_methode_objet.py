#!/usr/bin/python3
# -*- coding: latin-1 -*-

#Mon main
import controleurs_Bases
import CreationTable_O

monControleur = controleurs_Bases.ControleurBDSqlite("mabase")
monTableau = monControleur.ouvrirConnexion()
print(monTableau[0],monTableau[1])
#création de la requete pour la table Communes
req = '''CREATE TABLE IF NOT EXISTS Communes(
id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
Nom TEXT,
Code_Postal TEXT);'''
#nom de la table
table = "Communes"

maTable= CreationTable_O.TableSqlite(req,table,monTableau)
maTable.creationTable()

