"""
    File : diff.py
    Author : Tefang Ivan
    email : ivan.tefang@uha.fr
"""


import pandas as pds
import numpy as np
df=pds.read_csv('sae15\data/raw\energy-125-12-4_8.csv')
premier=(df.iloc[-1,3])
df=pds.read_csv('sae15\data/raw\energy-125-7-4_8.csv')
deuxieme=(df.iloc[-1,3])
diff= premier - deuxieme


print()
print("La derniére valeur du premier fichers est :", round(premier, 2))
print()
print("La derniére valeur du deuxieme fichers est :", round(deuxieme,2))
print()
print("la difference de consommation energetique entre les deux fichers est :", round(diff, 2))
print()
