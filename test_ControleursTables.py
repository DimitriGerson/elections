#!/usr/bin/python3
# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest import main as utmain
from ControleursBases import ControleurBDSqlite
from ControleursTables import InterrogeTable
from CreationTable import TableSqlite
from sqlite3 import Connection,Cursor
nomBase = "base_test_InterrogeTable"

class TestInterrogeTable(TestCase):

    def setUp(self):
        pass

    def test_controleurTableNone(self):
        """Test que le controleur de l'objet de classe InterrogeTable
        est egal à None."""
        question=InterrogeTable(1)  # 1 est choisit de façon totalement arbitraire
                                    #l'idée étant de mettre un paramètre non valide
        self.assertEqual(question.controleur,None)#Je pourrais aller plus loin dans la deffinition de l'utilisation 

    def test__init__(self):
        """Test que l'objet créer est bien de la
        classe InterrogeTable"""
        controleur = ControleurBDSqlite(nomBase)
        tableau = controleur.ouvrirConnexion()
        uneTable= InterrogeTable(tableau)
        controleur.fermerConnexion(tableau)
        self.assertIsInstance(uneTable,InterrogeTable)
        
    
    def test_ajoutLigneTable_OK(self):
        """Test de fonctionnement de fonction ajouterLigneTable dans le
        cas ou tout se passe bien"""
        monTest = ControleurBDSqlite(nomBase)
        tableau = monTest.ouvrirConnexion()
        uneTable = InterrogeTable(tableau)
        req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        table = "Communes"
        bob = TableSqlite(req,table,tableau)
        bob.creationTable()
        requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        monTuple = ('Paris',75000)
        marequete = uneTable.ajoutLigneTable(requete,monTuple)
        resp=uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Paris';''').fetchone()
        monTest.fermerConnexion(tableau)
        self.assertEqual(resp,(1,))

    def test_ajoutLigneSansCommit(self):
        """Ajout d'une ligne sans commit la ligne est donc visible
        tant que la connexion avec la base reste établi."""
        controleur = ControleurBDSqlite(nomBase)
        tableau = controleur.ouvrirConnexion()
        uneTable = InterrogeTable(tableau)
        req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        table = "Communes"
        bob = TableSqlite(req,table,tableau)
        bob.creationTable()
        requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        monTuple = ('Miami',280000)
        uneTable.ajoutLigneSansCommit(requete,monTuple)
        resp=uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Miami';''').fetchone()
        controleur.fermerConnexion(tableau)
        
        controleur = ControleurBDSqlite(nomBase)
        tableau = controleur.ouvrirConnexion()
        uneTable = InterrogeTable(tableau)
        resp2=uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Miami';''').fetchone()
        controleur.fermerConnexion(tableau)
        
        #la ligne resp existe-elle ? Oui
        self.assertEqual(resp,(1,))
        #la ligne resp2 existe-elle ? Non
        self.assertEqual(resp2,None)

    def test_faireCommit(self):
        """Pour faire un commit il faut donc faire un appel à la methode
        ajoutLigneSansCommit() puis faire un commit quitter la base puis
        se reconnecter à la base pour voir si le commit a été réalisé.
        Je rajoute un ajout de ligne sans commit et une déconnexion pour
        bien montrer que ajouterLigneSansCommit() fait vraiment l'ajout
        d'une ligne sans commit()"""
        controleur = ControleurBDSqlite(nomBase)
        tableau = controleur.ouvrirConnexion()
        uneTable = InterrogeTable(tableau)
        requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        monTuple = ('Chabris',36110)
        uneTable.ajoutLigneSansCommit(requete,monTuple)
        controleur.fermerConnexion(tableau)
        
        controleur = ControleurBDSqlite(nomBase)
        tableau = controleur.ouvrirConnexion()
        uneTable = InterrogeTable(tableau)
        resp=uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Chabris';''').fetchone()
        controleur.fermerConnexion(tableau)
        self.assertEqual(resp,None)
        

        controleur = ControleurBDSqlite(nomBase)
        tableau = controleur.ouvrirConnexion()
        uneTable = InterrogeTable(tableau)
        requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        monTuple = ('Lourdeix',36880)
        uneTable.ajoutLigneSansCommit(requete,monTuple)
        uneTable.faireCommit()
        controleur.fermerConnexion(tableau)
        controleur2 = ControleurBDSqlite(nomBase)
        tableau2 = controleur2.ouvrirConnexion()
        uneTable2 = InterrogeTable(tableau2)
        resp2=uneTable2.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Lourdeix';''').fetchone()
        self.assertEqual(resp2,(2,))

        
    def test_interrogeTable_NOK(self):
        """Interrogation de la base qui ne trouve rien."""
        controleur = ControleurBDSqlite(nomBase)
        tableau = controleur.ouvrirConnexion()
        uneTable = InterrogeTable(tableau)
        resp2=uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Miami';''').fetchone()
        controleur.fermerConnexion(tableau)
        self.assertEqual(resp2,None)
        
    def test_interrogeTable_OK(self):
        """Interrogation de la base qui ne trouve quelque chose."""
        controleur = ControleurBDSqlite(nomBase)
        tableau = controleur.ouvrirConnexion()
        uneTable = InterrogeTable(tableau)
        resp3=uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Lourdeix';''').fetchone()
        controleur.fermerConnexion(tableau)
        self.assertEqual(resp3,(2,))
        
if __name__ == '__main__':
    utmain()
