import pandas as pd

def add(ds1, ds2):
    ser1 = pd.Series(ds1)
    ser2 = pd.Series(ds2)
    return ser1 + ser2


def subtract(ds1, ds2):
    ser1 = pd.Series(ds1)
    ser2 = pd.Series(ds2)
    return ser1 - ser2


def multiply(ds1, ds2):
    ser1 = pd.Series(ds1)
    ser2 = pd.Series(ds2)
    return ser1 * ser2


def divide(ds1, ds2):
    ser1 = pd.Series(ds1)
    ser2 = pd.Series(ds2)
    return ser1 / ser2
