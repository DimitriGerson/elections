

#Les requetes d'insertion dans les tables

req_ins_Com='''INSERT INTO Communes(Nom,Code_Postal) VALUES (?,?);'''
req_ins_Scru="INSERT INTO Scrutins(Nom,Annee) VALUES (?,?);"
req_ins_TS="INSERT INTO Type_de_scrutins(Nom,ma_ref_Type_de_scrutin) VALUES (?,?);"
req_ins_Tours="INSERT INTO Tours(Numero_du_tour,ref_Scrutin) VALUES (?,?);"
req_ins_DG="INSERT INTO Donnees_generales(Inscrits,Abstentions,Votants,Blancs,Nuls,Exprimes,ref_Tour,ref_Commune) VALUES(?,?,?,?,?,?,?,?);"
req_ins_Partis="INSERT INTO Partis(Nom,Tendance) VALUES(?,?);"
req_ins_Cand="INSERT INTO Candidats(Nom,ref_Parti) VALUES(?,?);"
req_ins_RC="INSERT INTO Resultat_candidats(Nombre_de_voix,ref_Candidat,ref_Parti,ref_Tour,ref_Commune) VALUES(?,?,?,?,?);"
req_ins_Adj="INSERT INTO Adjoints(Nom,ref_Candidat) VALUES(?,?);"


def selectWhereSqlite(selection, table, premiereColo="",pValeur="",operateur="",deuxiemeColo="", dValeur="",WHERE="WHERE" ):

    if operateur != "":
        reste = " " + operateur + " " + deuxiemeColo + "=" + "'" + dValeur +"'"
    else:
        reste = " "
    if WHERE == "WHERE":
        retour = "SELECT " + selection + " FROM " + table + " " + WHERE + " " + premiereColo + "="+ "'" + pValeur + "'"+ reste + ";"
    else:
        retour = "SELECT " + selection + " FROM " + table + ";"
    return retour

req_sel_Com='''SELECT id_Commune FROM Communes WHERE Nom='Montreuil';'''
#drôle de requete...
