
rem Ma premiere remarque
echo Voici le script qui va me permettre de lancer mes test en python3
echo
rem python3 -v C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\controleurs_Bases.py
python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\ControleursBases.py
python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\CreationTable.py

rem python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\controleursBases.py

echo


python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\test_ControleursBases.py
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\une_base.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\mabase_test.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\base.db 
echo Nettoyage des bases de données créés lors des tests par suppression 
pause
rem lance tous les fichiers du type test_quelquechose.py python -m unittest discover
rem /s pour rechercher dans les sous-dossiers
