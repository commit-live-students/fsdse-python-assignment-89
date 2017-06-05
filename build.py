import pandas as pd


def add(ds1, ds2):
    """
    Enter your code here
    """
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    addSeries = ds1.add(ds2)
    addSeries = list(addSeries)
    return addSeries


def subtract(ds1, ds2):
    """
    Enter your code here
    """
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    addSeries = ds1.subtract(ds2)
    addSeries = list(addSeries)
    return addSeries


def multiply(ds1, ds2):
    """
    Enter your code here
    """
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    addSeries = ds1.multiply(ds2)
    addSeries = list(addSeries)
    return addSeries


def divide(ds1, ds2):
    """
    Enter your code here
    """
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    addSeries = ds1.divide(ds2)
    addSeries = list(addSeries)
    return addSeries

subtract([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
