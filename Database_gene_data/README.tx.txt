/*********************************************************************************
Title: README.txt
Authors: Jeong Yang & Tasdique Chowdhury
Date: 3/22/2017
Description: A text file containing information that is needed in order to run the
Python script
Purpose: To provide and educate the audience on running this source code
Modification: No modification is made in this text file


*********************************************************************************/




Prerequiste programs needed to run this source code:
-Python 3.6 (used PyCharm as IDE)
-Mongodb community edition (Current Version as of date)
-MYSQL community edition (Current Version as of date) // We did not use this database but the purpose of this is to parse the uniprot-human.xml file and getting certain data and putting into a table form in MYSQL
-NEO4j community edition (Current Version as of date)





Input Files: 
patients.csv
ROSMAP_RNASeq_entrez.csv
uniprot-human.xml
mongodb.py
biogrid file


In order for the mongodb.py to work within the USER favor:

mongoimport patients.csv in the patients database in the patients collection
mongoimport ROSMAP_RNASeq_entrez.csv in the patients database in the entrez collection


Also, you MUST convert the biogrid into csv provided in this folder






