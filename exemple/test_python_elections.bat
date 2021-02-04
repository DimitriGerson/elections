
rem Ma premiere remarque
echo Voici le script qui va me permettre de lancer mes test en python3
echo
rem python3 -v C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\controleurs_Bases.py
python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\ControleursBases.py
python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\CreationTable.py

rem python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\controleursBases.py

echo

echo o|del C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\bobi.db 

echo python3 C:\Dimitri\Formation_CA_2019-2020\python_Sqlite\Elections\base_de_donnees\test_ControleursBases.py
pause
rem lance tous les fichiers du type test_quelquechose.py python -m unittest discover
rem /s pour rechercher dans les sous-dossiers
