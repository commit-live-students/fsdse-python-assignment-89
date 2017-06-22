import pandas as pd


def add(ds1, ds2):
    return pd.Series.add(ds1,ds2)


def subtract(ds1, ds2):
    return pd.Series.subtract(ds1,ds2)


def multiply(ds1, ds2):
    return pd.Series.multiply(ds1,ds2)



def divide(ds1, ds2):
    return pd.Series.divide(ds1,ds2)
