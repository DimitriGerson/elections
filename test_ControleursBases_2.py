import unittest

from ControleursBases import ControleurBDSqlite
from sqlite3 import Connection,Cursor

class TestControleurBDSqlite(unittest.TestCase):

    def setUp(self):
        """pour commencer chaque methode"""
        nomBase ="une_base"
        self.monTest = ControleurBDSqlite(nomBase)
        

    def tearDown(self):
        """nettoyage à la fin de chaque methode"""
        print('Nettoyage !')
        
    def test_NotControleurBDSqlite(self):
        """Test que l'objet ControleurBDSqlite n'existe pas"""
        
        self.monTest = 1
        
        self.assertNotIsInstance(self.monTest,ControleurBDSqlite)

    def test_init_(self):
        """Test que l'objet créer est bien de la
        classe ControleurBDSqlite"""
        self.assertIsInstance(self.monTest,ControleurBDSqlite)


    
    def test_ouvrirConnexion_OK(self):
        """Test de fonctionnement de la connexion avec
        son connecteur"""
        monConnecteur = self.monTest.ouvrirConnexion()

        self.assertIsInstance(monConnecteur,tuple)
        self.assertIsInstance(monConnecteur[0],Connection)
        self.assertIsInstance(monConnecteur[1],Cursor)

    def test_ouvrirConnexion_NomVide(self):
        """Creation d'un objet de la classe ControleurBDSqlite avec
        un nom vide"""
        nomBase =""
        self.monTest = ControleurBDSqlite(nomBase)
        monConnecteur = self.monTest.ouvrirConnexion()
        self.assertIsInstance(monConnecteur,tuple)


    def test_fermerConnexion(self):
        """Procédure de fermeture de la connexion à la bdd"""
        monConnecteur = self.monTest.ouvrirConnexion()
        self.monTest.fermerConnexion(monConnecteur)
        self.assertIsInstance(monConnecteur,tuple)
        self.assertIsInstance(monConnecteur[0],Connection)
        self.assertIsInstance(monConnecteur[1],Cursor)

    def test___str__(self):
        """Redefinition de la methode __str__()"""
        self.assertEqual(self.monTest.__str__(),'une_base.db')

    def test___del__(self):
        """Redefinition de la methode __del__()"""
        del self.monTest
        self.assertIsNotNone(TestControleurBDSqlite)

if __name__ == '__main__':
    unittest.main()
