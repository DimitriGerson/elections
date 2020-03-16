colonne='id_Commune' #liste de colonne à retourner
motCle=" FROM " #liste de mot clé
table= "Commune" #liste des tables
motCle2 = " WHERE " #mot clé
motCle3= "Nom='" #colonne de table de la requete
case='Montreuil' #recherche
Close="'SELECT " #type de requete
def maConcaRequete(Close,colonne,motCle,table,motCle2,motCle3,case):

    bob=Close + colonne + motCle + table + motCle2 + motCle3 + case +"';'"
    return bob

print (maConcaRequete(Close,colonne,motCle,table,motCle2,motCle3,case))
