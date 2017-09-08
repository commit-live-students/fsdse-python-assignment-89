import pandas as pd

def add(ds1, ds2):
    ad = pd.Series.add(ds1,ds2)
    return ad

def subtract(ds1, ds2):
    s = pd.Series.subtract(ds1,ds2)
    return s

def multiply(ds1, ds2):
    mul = pd.Series.multiply(ds1,ds2)
    return mul

def divide(ds1, ds2):
    div = pd.Series.divide(ds1,ds2)
    return div

a = [1,3,5,7]
b = [2,4,6,8]
a1 = pd.Series(a)
b1 = pd.Series(b)
print add(b1,a1)
