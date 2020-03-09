#from sqlite3 import Connection
import sqlite3
def creationTable(requete, nomTable,curs,conn):

    """
    Cette fonction permet d'envoyer une requete lors de la création d'une table

    Elle prend en parametres requete qui est une requete Sqlite3, le nom de la table
    le curseur et la connexion
    param requete: requete en Sqlite3
    param nomTable: nom de la table
    param curs: le curseur pour la base de données
    param conn: le connecteur pour la base de données
    type requete: string
    type nomTable: string
    type curs: sqlite3.Cursor
    type conn: sqlite3.Connection
    :return: Des print
    :rtype: str

    
    Example:
    >>> conn =sqlite3.connect("Les_elections.db")
    >>> curs = conn.cursor()
    >>> req = '''CREATE TABLE IF NOT EXISTS Communes(id_Commune INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, Nom TEXT, Code_Postal TEXT);'''
    >>> table = "Communes"
    >>> creationTable(req,table,curs,conn)
    Création de la table Communes
    fin de procédure de création de la table Communes.
    La table Communes a au moins une ligne.
    

    .. seealso:: Référence à une autre partie du code
    .. warning:: Avertissement
    .. note:: Note
    .. todo:: Les test Units

    """
    
    try:
        curs.execute(requete)
        conn.commit()
        print("Création de la table " + nomTable)
    except sqlite3.OperationalError:
        print("Erreur la table " + nomTable + " n'a pas été trouvée")
    except Exception as e:
        print("!!! Une erreur s'est produite lors de la création de la table" + nomTable + ".")
        conn.rollback()
    finally:   
        print("fin de procédure de création de la table " + nomTable + ".")
    
    try:
        curs.execute ("SELECT * FROM " + nomTable + ";")
    except Exception as e:
        print("Une erreur est survenue lors de la creation de la table : " + nomTable )
        print("Erreur de type : " + e)
    finally:
        try :
            if curs.fetchone()[0]==1:
                print("La table " + nomTable + " a au moins une ligne.")
        except Exception as e:
            print("La table " + nomTable + " est vide !")

    #import doctest
    #doctest.testmod()
# A la fin de votre script, mettez ce snippet qui va activer les doctest
if __name__ == "__main__":
    print("Bonjour")
    import doctest
    doctest.testmod()
    print("Les tests ont été effectués")
    
