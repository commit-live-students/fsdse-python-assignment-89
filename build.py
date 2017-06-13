import pandas as pd


def add(ds1, ds2):
    """
    Enter your code here
    """
    return pd.Series(ds1)+pd.Series(ds2)

def subtract(ds1, ds2):
    """
    Enter your code here
    """
    return pd.Series(ds1)-pd.Series(ds2)

def multiply(ds1, ds2):
    """
    Enter your code here
    """
    return pd.Series(ds1)*pd.Series(ds2)


def divide(ds1, ds2):
    """
    Enter your code here
    """
    return pd.Series(ds1)/pd.Series(ds2)
