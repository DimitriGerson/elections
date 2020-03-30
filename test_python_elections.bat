
rem Ma premiere remarque
echo Voici le script qui va me permettre de lancer mes test en python3
echo
rem python3 -v C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\controleurs_Bases.py
python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\ControleursBases.py
python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\CreationTable.py

rem python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\controleursBases.py

echo


python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\test_ControleursBases_2.py
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\une_base.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\mabase_test.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\base.db 
echo Nettoyage des bases de donnees crees lors des tests par suppression 
pause
rem lance tous les fichiers du type test_quelquechose.py python -m unittest discover
rem /s pour rechercher dans les sous-dossiers
