liste=[]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df= pd.read_csv("data/raw/trier.csv")
df.plot(y='File Main Energy (J)', x='Timestamp (S)')