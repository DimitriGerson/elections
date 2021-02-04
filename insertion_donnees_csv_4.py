#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv, sqlite3
from requete import req_ins_Com,req_ins_DG,req_ins_RC,req_ins_Tours,selectWhereSqlite
from donnee import monTableau, table_nom,nomListeExiste
from remplir_base import rechercheIdTableDansListe,nomTableDepuisListe_ref, table_donnees,compareDeuxValeurs_AvecArret   #table donnees est une table qui représente la base à un instant t
                                                                                            #elle est chargées au début de ce script et donc ce script doit être
                                                                                            #le seul à modifier la base pendant la durée du script
                                                                                            #pas d'accés concurentiel,
#constantes
type_de_scrutin="Presidentielles" #j'ai besoin de cette valeur pour me fournir id du scrutin c'est l'une des données pour la référence au tour(premier second)
annee_scrutin=2017 #j'ai besoin de cette autre valeur pour me fournir id du scrutin c'est l'une des données pour la référence au tour(premier second)
#avec ces deux valeur j'obtiens une reférence à scrutin son type_de_scrutin(exemple: "Presidentielles" et son année exemple:2017)

#Si on recherche un scrutin le fait d'aller dans la table Scrutins semble évident.
table_Scru="Scrutins"#Pas trouvé mieux
#pourquoi j'ai besoin de id du scrutin ?
#C'est l'une des données pour avoir la référence au tour. J'en aurai besoin pour toutes les requetes.

table_Scrutins=nomTableDepuisListe_ref(req_ins_Tours)#attention c'est un tableau pas une valeur directement
print(table_Scrutins)
compareDeuxValeurs_AvecArret(table_Scru,table_Scrutins[0])#Verification que la table Scrutins s'écrit bien ainsi 

id_scru=rechercheIdTableDansListe(table_donnees,table_Scru,type_de_scrutin, valeur_2=annee_scrutin) #retour de l'id du bon scrutin j'en aurai besoin pour référencer les tours
# retourne l'id du scrutin "Présidentielles 2017" dans la liste des Scrutins attention il s'agit bien d'une liste des scritns(pas une table dans une base de données)
# j'aurai pu faire une requête SQLITE pour récupérer l'id mais je souhaite partir d'un tableau hors connexion dans quel but ? avec selectWhereSqlite(selection, table, premiereColo="",pValeur="",operateur="",deuxiemeColo="", dValeur="",WHERE="WHERE" )
table_Ins = nomListeExiste("Resultat_candidats")    #pour changer la table d'insersion venir ici elle vérifie que le nom
                                                    #de la table existe dans table_nom
                                                    #et renvoie le nom passé en argument s'il existe dans la table_nom
req_Ins=req_ins_RC #pour changer la requete pour l'insersion venir ici
listeRefTables=nomTableDepuisListe_ref(req_Ins)#creation d'une liste des noms de tables de ref utilisées par la requête req_Ins
listeRefTables.append(table_Scrutins[0])#ajout de "Scrutins" pour la table Scrutins à la liste listeRefTables C'est bon jusqu'ici !
# listeRefTables : ['Candidats', 'Partis', 'Tours', 'Communes', 'Scrutins']

#Ici commence la lecture du fichier csv...
with open('Aubervilliers.csv','r') as fin: # `with` statement available in 2.5+
    dr = csv.reader(fin) # comma is default delimiter
    print(dr)
    DG=[] #tableau des données générales
    TableDG=0
    TableRC=0
    a=0 #représente la ligne où se trouve le curseur pour le fichier .csv
    tableau_requetes=[]
    
    for i in dr:
        a=a+1
        if a==1:
            pass#pas d'info en première ligne ?
        if a==2:
            table=i[0]#ici j'ai le nom de la commune et je veux son id
            com_id =rechercheIdTableDansListe(table_donnees,listeRefTables[3],i[0])#listeRefTables[3] : Communes, i[0] : Nom de la commune si celui-ci se trouve à la deuxième ligne première colonne ligne du fichier .csv
        elif a==3:
            pass
        elif a==4:
            #cette succession de commandes fonctionne pour récupérer des données depuis la bdd via un tableau table_donnees pour aller chercher des données dans un csv
            #pour les ordonner pour créer des requêtes.
            #il faudra peut-être rajouter une étape pour que cela soit compréhensible
            #les requetes seront ensuite transmises à la bdd pour insérées ces nouvelles données à leurs tours dans la base de données.
            #il faut que j'ordonne cette succession de commande pour en faire au moins une fonction au mieux une classe
            tour=2 #pour une reference au tour
            #je dois faire une fonction qui renvoie la requete req
            #les param d'entrée sont table_donnees,listeRefTables[0],i[0],changeColonne=2,listeRefTables[2],tour,valeur_2=id_scru
            list_sec=[]
            list_sec.append(i[1])#le nombre de voix
            ref_Can=rechercheIdTableDansListe(table_donnees,listeRefTables[0],i[0])#interrogation de ma liste pour avoir la ref au candidat i[0] étant le nom du candidat
            ref_Parti=rechercheIdTableDansListe(table_donnees,listeRefTables[0],i[0],changeColonne=2)#la reférence du parti via le nom du Candidat retourne ref_parti
            ref_Tour=rechercheIdTableDansListe(table_donnees,listeRefTables[2],tour,valeur_2=id_scru)#pour avoir la ref au tour listeRefTables[2]:"Tours"
            #Ajout des données à list_sec
            list_sec.append(ref_Can)
            list_sec.append(ref_Parti)
            list_sec.append(ref_Tour)
            list_sec.append(com_id)
            #Création de la requete
            req=(req_Ins,list_sec,table_Ins)
            #Ajout de la requête au tableau de requetes
            tableau_requetes.append(req)
        elif a==5: 
            req=(req_ins_RC,i,tableIns)
            liste_sec=[]
            #ajouter les resultat en premier
            liste_sec.append(i[1])
            #grace au nom trouver id du candidat
            idCandidat=rechercheIdTableDansListe(table_donnee,table,i[0])
            #il faut transformer le nom du candidat en ref au candidat
            #il faut trouver la reference au parti
            #il faut trouver la reference au tour
            #il faut trouver la reference à la commune
            tableau_requetes.append(req)
        elif a==6:
            tableDG=i[0]
        elif a==7:
            DG.append(i[1])
        elif a==8:
            DG.append(i[1])
        elif a==9:
            DG.append(i[1])
        elif a==10:
            DG.append(i[1])
        elif a==11:
            DG.append(i[1])
        elif a==12:
            DG.append(i[1])
        elif a==13:
            DG.append(i[0])
        elif a==14:
            DG.append(i[0])
            req=(req_ins_DG,DG,tableDG)
            tableau_requetes.append(req)
            print("fin du second tour")
        elif a==15:
            pass#j'ai déjà le Table
        elif a==16:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==17:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==18:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==19:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==20:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==21:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==22:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==23:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==24:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==25:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==26:
            req=(req_ins_RC,i,tableRC)
            tableau_requetes.append(req)
        elif a==27:
            pass
        elif a==28:
            DG=[]
            DG.append(i[1])
        elif a==29:
            DG.append(i[1])
        elif a==30:
            DG.append(i[1])
        elif a==31:
            DG.append(i[1])
        elif a==32:
            DG.append(i[1])
        elif a==33:
            DG.append(i[1])
        elif a==34:
            DG.append(i[0])
        elif a==35:
            DG.append(i[0])
            req=(req_ins_DG,DG,tableDG)
            tableau_requetes.append(req)
            print("fin du premier tour")
            
            
            
            
            
    for ele in tableau_requetes:
        print("Un element")
        print (ele)
        for o in ele:
            
            print(o)
#ecriture dans un fichier qui portera le nom de la commune
mon_fichier = open("Aubervillier.txt", "w") # Argh j'ai tout écrasé !
mon_fichier.write(str(tableau_requetes))
mon_fichier.close()

mon_fichier = open("Aubervillier.txt", "r")
contenu = mon_fichier.read()
print('impression du contenu')
print(contenu)
mon_fichier.close()


#cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
#con.commit()
#con.close()
