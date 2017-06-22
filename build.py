import pandas as pd

ds_o = pd.Series()

def add(ds1, ds2):
    ds_o = ds1+ds2
    return ds_o

def subtract(ds1, ds2):
    ds_o = ds1-ds2
    return ds_o


def multiply(ds1, ds2):
    ds_o = ds1*ds2
    return ds_o


def divide(ds1, ds2):
    ds_o = ds1/ds2
    return ds_o

dsa = pd.Series([1,2,3,4])
dsb = pd.Series([4,5,6,7])

add(dsa,dsb)
subtract(dsb,dsa)
multiply(dsa,dsb)
divide(dsa,dsb)
