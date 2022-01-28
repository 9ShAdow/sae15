"""
    File : sae.py
    Author : Bahir Boudouma-Lambarki
    email : bahir.boudouma-lambarki@uha.fr
"""

import pandas as pds

desc = open("test.csv", "w")
desc = open("energy-125-7-4_6.csv","r")
content = desc.readlines()
for idx in content :
    desc = open("test.csv", "a")
    desc.write(idx)
desc.close()


