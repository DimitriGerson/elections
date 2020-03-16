#dans ce fichier je vais rentrer les resultats des présidentielles 2017
#je les tables sont toutes créées je peux commencer par faire une rapide intérogation
#de toutes les tables puis rentrer les fichiers depuis un dossier sources

from requete import selectWhereSqlite,req_ins_Scru,req_ins_Partis,req_ins_Cand

from donnee import monTableau, base, table_nom
import sqlite3
import csv

#Controleur de la création de table
#Son role est de créer les tables
from CreationTable import TableSqlite as TS
from ControleursBases import ControleurBDSqlite as BD

#interogation de la base pour voir si les tables sont là et ce qu'elles ont dedans

table_donnees=[]
leControleur = BD(base)
#connexion = leControleur.ouvrirConnexion()
#maTable = TS(monTableau[1][0],monTableau[1][1],connexion)

for ele in monTableau:
    connexion = leControleur.ouvrirConnexion()
    maTable = TS(ele[0],ele[1],connexion)
    requete=selectWhereSqlite('*',ele[1], WHERE="")
    print(requete)
    table=maTable.interrogeTable(requete)
    a=table.fetchall()
    table_donnees.append(ele[1])
    table_donnees.append(a)
    
    leControleur.fermerConnexion(connexion)

#aller rechercher les fichiers puis les passer et les intégrer dans la base de données

a=table_donnees.index('Scrutins')
b=table_donnees[a+1]
for ele in b:
    if ele[1]=="Presidentielles" and ele[2]==2017:
        print(ele[0])
#intéroger la base de données
def rechercheIdTableDansListe(liste,table,valeur_1,valeur_2="",changeColonne=0):
    a=liste.index(table)
    b=liste[a+1]

    if valeur_2=="":
        print("je passe ici 1")
        for ele in b:
            print(ele)
            if ele[1].lower() ==valeur_1.lower():
                print("je passe ici 3")
                monId=(ele[changeColonne])
    else:
        for ele in b:
            print("toto")
            print(ele[1])
            print(ele[2])
            if ele[1]==valeur_1 and ele[2]==valeur_2:
                print("dis_moi oui")
                monId=(ele[changeColonne])
    return monId

bob = rechercheIdTableDansListe(table_donnees,'Candidats','Emmanuel Macron',changeColonne=2)

print(bob)
print(table_donnees)

#je veux récupérer les nom des tables grâce à la requete elle-même en récupérant
#le nom des tables qui se trouvent dans id des tables.
def nomTableDepuisListe_ref(laRequeteEntiere):
    #Les lignes qui suivent ont pour but de récupérer les nom des tables dont
    #on aura besoin pou la requete req_Ins pour ne pas à avoir
    #à les écrire en dur dans les tables nommées table_Scru etc...
    #C'est la partie de la requete concernant les valeur à insérer
    #je récuère le nom des colonnes de la table pour la requete,
    #de cette façon je vais pouvoir trouver les bonnes données à rentrer
    mes_nomtables=laRequeteEntiere[(laRequeteEntiere.index("(")+1):laRequeteEntiere.index(")")]# les_variables de la requêtes req_Ins
    liste_ref=mes_nomtables[mes_nomtables.index("ref_"):]
    # de cette façon je récupère les_variables à partir du premier "ref_"
    #ce qui est important pour récupérer toutes les ref
    listes_nom_tables=[]
    for ele in liste_ref:
        a=liste_ref.index(ele)
        print(ele)
        print(liste_ref.index(ele))
        if ele == "_" and liste_ref[(a-1)] == "f" and liste_ref[(a-2)] == "e" and liste_ref[(a-3)] == "r":
            premierIndice_ = liste_ref.index(ele)#me renvoie le premier indice de "_" 
            liste_ref=liste_ref[(premierIndice_ + 1):]#de cette façon je réinitialise mes_nomtable avec une liste plus petite qui commence après ref_
            try:
                nomDeVariable=liste_ref[:liste_ref.index(',')]#je crée une variable qui a pour valeur le nom sans ref_ jusqu'à la première virgule
                nomDeVariable=nomDeVariable+"s" #Ce qui me donne le nom de la table
                listes_nom_tables.append(nomDeVariable)
            except ValueError: #quand il n'y a pas de virgule (le mot est le dernier)
                print("dernière valeur.")
                nomDeVariable = liste_ref + "s" #recupération de la dernière valeur à laquelle on rajoute un s pour créer le nom de table
                listes_nom_tables.append(nomDeVariable)


    return(listes_nom_tables)

def compareDeuxValeurs_AvecArret(valeur1,valeur2):
    if valeur1==valeur2:
        print("OK!")
    else:
        print("Problème")
        
        interuptiondeprogramme#si le programme crash ici c'est qu'il y a un problème qui empeche le code de fonctionner
    

