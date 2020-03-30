import unittest

from ControleursBases import ControleurBDSqlite
from ControleursTables import InterrogeTable
from sqlite3 import Connection,Cursor

class TestInterrogeTable(unittest.TestCase):

    def setUp(self):
        pass

    def test_NotControleurBDSqlite(self):
        """Test que l'objet ControleurBDSqlite n'existe pas"""
        
        monTest = 1
        
        self.assertNotIsInstance(monTest,InterrogeTable)

    def test_init_(self):
        """Test que l'objet créer est bien de la
        classe ControleurBDSqlite"""
        controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        tableau = controleur.ouvrirConnexion()
        monTest = ControleursTables.InterrogeTable(tableau)

        self.assertIsInstance(monTest,ControleursTables)


    
    def test_ajoutLigneTable_OK(self):
        """Test de fonctionnement de la connexion avec
        son connecteur"""
        pass
        nomBase ="une_base"
        monTest = ControleurBDSqlite(nomBase)
        monConnecteur = monTest.ouvrirConnexion()

        self.assertIsInstance(monConnecteur,tuple)
        self.assertIsInstance(monConnecteur[0],Connection)
        self.assertIsInstance(monConnecteur[1],Cursor)

    def test_ajoutLigneSansCommit(self):
        pass
        nomBase =""
        monTest = ControleurBDSqlite(nomBase)
        monConnecteur = monTest.ouvrirConnexion()
        
        monConnecteur = monTest.ouvrirConnexion()

        self.assertIsInstance(monConnecteur,tuple)


    def test_faireCommit(self):
        pass
        nomBase ="une_base"
        monTest = ControleurBDSqlite(nomBase)
        monConnecteur = monTest.ouvrirConnexion()
        monTest.fermerConnexion(monConnecteur)
        

        self.assertIsInstance(monConnecteur,tuple)
        self.assertIsInstance(monConnecteur[0],Connection)
        self.assertIsInstance(monConnecteur[1],Cursor)
        
    def test_interrogeTable(self):
        pass
if __name__ == '__main__':
    unittest.main()
