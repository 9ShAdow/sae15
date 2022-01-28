'''import pandas as pd
df = pd.read_csv("sae15\data/raw\energy-125-7-4_5.csv", encoding='ISO-8859-1', sep=',')
x = pd.isnull(df).sum().sum()
pourcent = (x / (5 * 'Remplacez par le nombre de lignes du ficher (2682789 pour le fichier saedoc.csv par exemple et 210614 pour le ficher energy-125-7-4_5.csv)' )) * 100
print()
print("Le nombre de valeurs manquantes est de", x)
print()
print("Le pourcentage des valeurs manquantes est de", round(pourcent, 2), "%")
print()

rempli = (5 * 'Remplacez par le nombre de lignes du ficher (2682789 pour le fichier saedoc.csv par exemple et 210614 pour le ficher energy-125-7-4_5.csv))') - x

print("On a des valaurs dans ",rempli, "cases")
print()
'''

#pour observer les valeures manquantes dans chaque observation l suffit de changer
# le chemins d'acces et de mettre celui du ficher souhaité
#le ficher commun (toutes les données reunis ) est le saedoc.csv

# Exemple Pratique 

import pandas as pd
df = pd.read_csv("sae15\data/raw\energy-125-7-4_5.csv", encoding='ISO-8859-1', sep=',')
x = pd.isnull(df).sum().sum()
pourcent = (x / (5 * 210614 )) * 100
print()
print("Le nombre de valeurs manquantes est de", x)
print()
print("Le pourcentage des valeurs manquantes est de", round(pourcent, 2), "%")
print()

rempli = (5 * 210614) - x

print("On a des valaurs dans ",rempli, "cases")
print()