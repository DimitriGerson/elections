
rem Ma premiere remarque
echo Voici le script qui va me permettre de lancer mes test en python3
echo
rem python3 -v C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\controleurs_Bases.py
py C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\ControleursBases.py
pause
py C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\CreationTable.py
pause
py C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\ControleursTables.py
pause
rem python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\controleursBases.py

echo


py C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\test_ControleursBases.py
pause
py C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\test_ControleursTables.py
pause
py C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\test_CreationTable.py
pause
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\base.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\base_Test_ControleurBDSqlite.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\base_test_InterrogeTable.db 
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\base_test_TableSqlite.db
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\mabase_test.db
echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\Presidentielle_2017\dossier21032020\MAJ\version_31_mars\nouvelle_bdd.db
echo Nettoyage des bases de donnees crees lors des tests par suppression 

pause
rem lance tous les fichiers du type test_quelquechose.py python -m unittest discover
rem /s pour rechercher dans les sous-dossiers
