import pandas as pd


def add(ds1, ds2):
    ds = ds1 + ds2
    return ds


def subtract(ds1, ds2):
    ds = ds1 - ds2
    return ds


def multiply(ds1, ds2):
    ds = ds1 * ds2
    return ds


def divide(ds1, ds2):
    ds = ds1 / ds2
    return ds

input1 = pd.Series([2, 4, 6, 8, 10])

input2 = pd.Series([1, 3, 5, 7, 9])

add(input1,input2)
subtract(input1,input2)
multiply(input1,input2)
divide(input1,input2)
