#!/usr/bin/python3
# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest import main as utmain
from ControleursBases import ControleurBDSqlite
from sqlite3 import Connection,Cursor

nomBase="base_Test_ControleurBDSqlite"
class TestControleurBDSqlite(TestCase):

    def setUp(self):
        """pour commencer chaque methode"""
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
        self.assertIsInstance(monConnecteur,tuple)
        self.assertIsInstance(monConnecteur[0],Connection)
        self.assertIsInstance(monConnecteur[1],Cursor)

    def test_ouvrirConnexion_NomVide(self):
        """Creation d'un objet de la classe ControleurBDSqlite avec
        un nom vide"""
        self.monTest = ControleurBDSqlite()
        monConnecteur = self.monTest.ouvrirConnexion()
        self.assertEqual(self.monTest.nom,'nouvelle_bdd.db')

    def test_fermerConnexion(self):
        """Procédure de fermeture de la connexion à la bdd"""
        monConnecteur = self.monTest.ouvrirConnexion()
        self.monTest.fermerConnexion(monConnecteur)
        self.assertIsInstance(monConnecteur,tuple)
        self.assertIsInstance(monConnecteur[0],Connection)
        self.assertIsInstance(monConnecteur[1],Cursor)

    def test___str__(self):
        """Redefinition de la methode __str__()"""
        self.assertEqual(self.monTest.__str__(),'base_Test_ControleurBDSqlite.db')

    def test___del__(self):
        """Redefinition de la methode __del__()"""
        del self.monTest
        
        with self.assertRaises(AttributeError):
            self.monTest

if __name__ == '__main__':
    utmain()