#!/usr/bin/python3
# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest import main as utmain
from ControleursBases import ControleurBDSqlite
from ControleursTables import InterrogeTable
from CreationTable import TableSqlite
from sqlite3 import Connection,Cursor
nomBase = "base_test_TableSqlite"

class TestTableSqlite(TestCase):

    def setUp(self):
        """Les donnees fixes"""
        self.controleur = ControleurBDSqlite(nomBase)
        self.tableau = self.controleur.ouvrirConnexion()
        self.req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        self.table = "Communes"
        self.maTable = TableSqlite(self.req,self.table,self.tableau)

    def test__init__(self):
        """Si mon objet est de la classe TableSqlite c'est bon"""
        self.controleur.fermerConnexion(self.tableau)
        self.assertIsInstance(self.maTable,TableSqlite)

    def test_creationTable_OK(self):
        """Si je peux envoyer une requete à la table et
        récupérer une valeur fixe c'est bon"""
        self.maTable.creationTable()
        requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        monTuple = ('Paris',75000)
        uneTable = InterrogeTable(self.tableau)
        marequete = uneTable.ajoutLigneTable(requete,monTuple)
        resp=uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Paris';''').fetchone()
        self.controleur.fermerConnexion(self.tableau)
        self.assertEqual(resp,(1,))
        
if __name__ == '__main__':
    utmain()
