import pandas as pd


def add(ds1, ds2):
    return ds1.add(ds2)
def subtract(ds1, ds2):
    return ds1.subtract(ds2)
def multiply(ds1, ds2):
    return ds1.multiply(ds2)
def divide(ds1, ds2):
    return ds1.divide(ds2)

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])

print(add(ds1,ds2))
print(subtract(ds1,ds2))
print(multiply(ds1,ds2))
print(divide(ds1,ds2))
