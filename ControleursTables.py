"""Je dois créer une classe qui soit la classe mère de TableSqlite"""

class InterrogeTable:

    def __init__(self,controleur):
        """
        param : controleur
        type : 'ControleursBases'
        :return
        :rtype: 'InterrogeTable'
        
        Example:
        >>> import ControleursBases
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>>
        """
        
        
        try:        
            if str(type(controleur)) == "<class 'tuple'>" :
                self.controleur=controleur
                print("1")
            else:
                print(type(controleur))
                self.controleur = None
                print("Votre controleur est nul.")
                del self
                print("objet détruit.")
        except:
            print("problème de controleur")
            print(type(controleur))
            del self
            print("objet détruit.")
        else:
            print("L'initialitation de la table est réalisée.")
        finally:
            print("Fin de d'initialisation de table.")

    def ajoutLigneTable(self,baserequete,ajout):
        """faire la doc
            la base de la requete est : 'INSERT INTO Resultat_candidats(Nombre_de_voix,ref_Candidat,ref_Parti,ref_Tour,ref_Commune) VALUES(?,?,?,?,?);'
            l'ajout est un tuple : (126, 4, 4, 1, 1127)
        param : baserequete
        type : str
        param : ajout
        type : tuple
        :return
        :rtype:
        Example:
        >>> import ControleursBases
        >>> import CreationTable
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = CreationTable.TableSqlite(req,table,tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        1
        2
        table réalisée.
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes est vide !
        >>> uneTable = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>> requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        >>> monTuple = ('Paris',75000)
        >>> uneTable.ajoutLigneTable(requete,monTuple)
        La requête s'est déroulée normalement.
        >>> controleur.fermerConnexion(tableau)
        La connexion est fermée
        Aucune erreur !
        Fin de la methode fermerConnexion()
        """
        #il faudrait que l'ajout de ligne se charge aussi de la connexion dans le cas où
        #il n'y a pas de connexion. c'est assez fragile en fait ici.
        try:
            self.controleur[1].execute(baserequete,ajout)
            self.controleur[0].commit()
        except Exception as e:
            print("Une erreur est survenue lors de l'ajout de la ligne.")
            print (e)
        else:
            print("La requête s'est déroulée normalement.")

    def ajoutLigneSansCommit(self,baserequete,ajout):
        """
        param : baserequete
        type : str
        param : ajout
        type : tuple
        :return
        :rtype:
        Example:
        >>> import ControleursBases
        >>> import CreationTable
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = CreationTable.TableSqlite(req,table,tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        1
        2
        table réalisée.
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes est vide !
        >>> uneTable = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>> requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        >>> monTuple = ('Marseille',13000)
        >>> uneTable.ajoutLigneSansCommit(requete,monTuple)
        La requête s'est déroulée normalement.
        """
        
        try:
            self.controleur[1].execute(baserequete,ajout)
        except Exception as e:
            print("Une erreur est survenue lors de l'ajout de la ligne.")
            print (e)
        else:
            print("La requête s'est déroulée normalement.")
        
    def faireCommit(self):
        """
        Example:
        >>> import ControleursBases
        >>> import CreationTable
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = CreationTable.TableSqlite(req,table,tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        1
        2
        table réalisée.
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes a au moins une ligne.
        >>> uneTable = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>> requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        >>> monTuple = ('Marseille',13000)
        >>> uneTable.ajoutLigneSansCommit(requete,monTuple)
        La requête s'est déroulée normalement.
        >>> uneTable.faireCommit()
        Commit réalisé.
        """
        
        try:
            self.controleur[0].commit()
        except Exception as e:
            print("Une erreur est survenue lors de la consultation de la bdd.")
            print (e)
        else:
            print('Commit réalisé.')
            
    def interrogeTable(self,requete):
        """Attention cette requete peut être potentiellement dangereuse si la requete passée n'est
        pas une interrogation de base.
        Rien n'empêche à ce niveau de passer une requete d'insertion.
        Example
        >>> import sqlite3
        >>> import ControleursBases
        >>> import CreationTable
        >>> import ControleursTables
        >>> controleur = ControleursBases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> print(type(controleur))
        <class 'ControleursBases.ControleurBDSqlite'>
        >>> bob = CreationTable.TableSqlite(req,table,tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        1
        2
        table réalisée.
        Fin de d'initialisation de table.
        >>> bob.creationTable()
        CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);
        Création de la table Communes
        Aucune erreur !
        fin de procédure de création de la table Communes.
        Aucune erreur lors de la création de la table !
        La table Communes a au moins une ligne.
        >>> uneTable = ControleursTables.InterrogeTable(tableau)
        1
        L'initialitation de la table est réalisée.
        Fin de d'initialisation de table.
        >>> requete = 'INSERT INTO Communes(Nom,Code_Postal) VALUES(?,?);'
        >>> monTuple = ('Marseille',13000)
        >>> uneTable.ajoutLigneSansCommit(requete,monTuple)
        La requête s'est déroulée normalement.
        >>> uneTable.faireCommit()
        Commit réalisé.
        >>> uneTable.interrogeTable('''SELECT id_Commune FROM Communes WHERE Nom='Marseille';''').fetchone()
        La requête s'est déroulée normalement.
        (2,)
        """
        if str(requete[0:6])=='SELECT':
            try:
                bob = self.controleur[1].execute(requete)
            except Exception as e:
                print("Une erreur est survenue lors de la consultation de la bdd.")
                print (e)
            else:
                print ("La requête s'est déroulée normalement.")
                return bob
            bob = None
            return bob
        else:
            print('Votre requete ne commence pas par "SELECT".')
            print(str(requete[0:6]))


#Ce snippet active les doctest et donc mes tests dans Example
if __name__ == "__main__":
    print("Bonjour")
    from doctest import testmod
    testmod()
    print("Les tests de la documentation ont été effectués")
