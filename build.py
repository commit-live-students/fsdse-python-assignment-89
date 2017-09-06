import pandas as pd
from pandas import Series

def add(ds1, ds2):
    return Series(ds1) + Series(ds2)


def subtract(ds1, ds2):
    return Series(ds1) - Series(ds2)



def multiply(ds1, ds2):
    return Series(ds1) * Series(ds2)



def divide(ds1, ds2):
    return Series(ds1) / Series(ds2)
