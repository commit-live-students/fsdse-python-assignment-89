import pandas as pd


def add(ds1, ds2):
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    addlist = ds1.add(ds2)
    print addlist
    return addlist

def subtract(ds1, ds2):
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    sublist = ds1.subtract(ds2)
    return sublist


def multiply(ds1, ds2):
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    mlplist = ds1.multiply(ds2)
    return mlplist


def divide(ds1, ds2):
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    divlist = ds1.divide(ds2)
    return divlist

print add([2, 4, 6, 8, 10],[1, 3, 5, 7, 9])
print subtract([2, 4, 6, 8, 10],[1, 3, 5, 7, 9])
print multiply([2, 4, 6, 8, 10],[1, 3, 5, 7, 9])
print divide([2, 4, 6, 8, 10],[1, 3, 5, 7, 9])
