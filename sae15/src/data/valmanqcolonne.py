"""
    File : valmanqcolonne.py
    Author : Tefang Ivan Boudouma Bahir
    email : ivan.tefang@uha.fr bahir.boudouma-lambarki@uha.fr
"""


'''import pandas as pd
df = pd.read_csv("sae15\data\processed/trier.csv", encoding='ISO-8859-1', sep=',')
x = pd.isnull(df.iloc[:,1(numero de la colonne souhaité)]).sum().sum()
pourcent = (x / (5 * 2682783)) * 100
print()
print("Le nombre de valeurs manquantes est de", x)
print()
print("Le pourcentage des valeurs manquantes est de", round(pourcent, 2), "%")
print()
'''


# Exemple Pratique 


import pandas as pd
df = pd.read_csv("sae15\data\processed/trier.csv", encoding='ISO-8859-1', sep=',')
x = pd.isnull(df.iloc[:,2]).sum().sum()
pourcent = (x / (5 * 2682783)) * 100
print()
print("Le nombre de valeurs manquantes est de", x)
print()
print("Le pourcentage des valeurs manquantes est de", round(pourcent, 2), "%")
print()