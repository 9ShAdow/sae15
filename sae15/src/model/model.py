import pandas as pds

def ComputeMean():
    mean = 0
    df= pds.read_csv("data/raw\s_titre_all.csv")
    x=df.iloc[:,1]

    print()
    print("La moyenne de la colonne File Main Current (A) est:",x.mean())
    print("")
    print()
    print()


    return (mean)
ComputeMean()





def ComputeMedian():
    median = 0

    df= pds.read_csv("data/raw\s_titre_all.csv")
    z=df.iloc[:,1]
    print()
    print("La médiane de la colonne File Main Current (A) est:", z.median())
    print("")
    print()

    return (median)
ComputeMedian()