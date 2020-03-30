import unittest

from ControleursBases import ControleurBDSqlite
from sqlite3 import Connection,Cursor

class TestControleurBDSqlite(unittest.TestCase):

    def setUp(self):
        self.simple_comme_bonjour = ('pomme', 'banane')

    def test_NotControleurBDSqlite(self):
        """Test que l'objet ControleurBDSqlite n'existe pas"""
        
        monTest = 1
        
        self.assertNotIsInstance(monTest,ControleurBDSqlite)

    def test_init_(self):
        """Test que l'objet créer est bien de la
        classe ControleurBDSqlite"""
        nomBase ="une_base"
        monTest = ControleurBDSqlite(nomBase)

        self.assertIsInstance(monTest,ControleurBDSqlite)


    
    def test_ouvrirConnexion_OK(self):
        """Test de fonctionnement de la connexion avec
        son connecteur"""

        nomBase ="une_base"
        monTest = ControleurBDSqlite(nomBase)
        monConnecteur = monTest.ouvrirConnexion()

        self.assertIsInstance(monConnecteur,tuple)
        self.assertIsInstance(monConnecteur[0],Connection)
        self.assertIsInstance(monConnecteur[1],Cursor)

    def test_ouvrirConnexion_NomVide(self):
        nomBase =""
        monTest = ControleurBDSqlite(nomBase)
        monConnecteur = monTest.ouvrirConnexion()
        
        monConnecteur = monTest.ouvrirConnexion()

        self.assertIsInstance(monConnecteur,tuple)


    def test_fermerConnexion(self):

        nomBase ="une_base"
        monTest = ControleurBDSqlite(nomBase)
        monConnecteur = monTest.ouvrirConnexion()
        monTest.fermerConnexion(monConnecteur)
        

        self.assertIsInstance(monConnecteur,tuple)
        self.assertIsInstance(monConnecteur[0],Connection)
        self.assertIsInstance(monConnecteur[1],Cursor)
        

if __name__ == '__main__':
    unittest.main()
