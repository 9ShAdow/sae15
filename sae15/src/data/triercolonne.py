import pandas as pd
import csv
import numpy as np
ls=[]
with open('U:/Documents/lora-energie-transmission/data/raw/saedoc.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        df=('; '.join(row))
        ls.append(df)
np.savetxt('saedoctrier.csv',ls,delimiter=';',fmt ='% s')