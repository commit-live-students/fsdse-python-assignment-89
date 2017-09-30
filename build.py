import pandas as pd


def add(ds1, ds2):
    return ds1 + ds2


def subtract(ds1, ds2):
    return ds1 - ds2

def multiply(ds1, ds2):
    return ds1 * ds2

def divide(ds1, ds2):
    return ds1 / ds2

s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

print add(s1, s2)
print subtract(s1, s2)
print multiply(s1, s2)
print divide(s1, s2)
