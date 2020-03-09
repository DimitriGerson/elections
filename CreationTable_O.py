#from sqlite3 import Connection
import sqlite3

class TableSqlite :
    def __init__(self,requete,nomTable,controleur):
        """
        Example:
        >>> import controleurs_Bases
        >>> import CreationTable_O
        >>> controleur = controleurs_Bases.ControleurBDSqlite("mabase_test")
        >>> tableau = controleur.ouvrirConnexion()
        ouverture de la connexion
        Clés étrangères activées
        Fin de la methode ouvrirConnexion()
        >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,Nom TEXT,Code_Postal TEXT);'''
        >>> table = "Communes"
        >>> bob = CreationTable_O.TableSqlite(req,table,controleur)
        1
        2
        3
        >>> print(type(bob))
        <class 'CreationTable_O.TableSqlite'>
        """
        self.requete=requete
        print("1")
        self.nomTable=nomTable
        print("2")
        self.controleur=controleur
        print("3")

        
    def creationTable(self):

        
        try:
            self.controleur[1].execute(self.requete)
            self.controleur[0].commit()
            print("Création de la table " + self.nomTable)
        except sqlite3.OperationalError:
            print("Erreur la table " + self.nomTable + " n'a pas été trouvée")
        except Exception as e:
            print("!!! Une erreur s'est produite lors de la création de la table" + self.nomTable + ".")
            self.controleur[0].rollback()
        finally:   
            print("fin de procédure de création de la table " + self.nomTable + ".")
    
        try:
            self.controleur[1].execute ("SELECT * FROM " + self.nomTable + ";")
        except Exception as e:
            print("Une erreur est survenue lors de la creation de la table : " + self.nomTable )
            print("Erreur de type : " + e)
        finally:
            try :
                if self.controleur[1].fetchone()[0]==1:
                    print("La table " + self.nomTable + " a au moins une ligne.")
            except Exception as e:
                print("La table " + self.nomTable + " est vide !")


#Ce snippet active les doctest et donc mes tests dans Example
if __name__ == "__main__":
    print("Bonjour")
    import doctest
    doctest.testmod()
    print("Les tests de la documentation ont été effectués")
    
