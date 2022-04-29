# Inputs
import numpy as np
import pandas as pd
'''
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# Solution
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)
print(ser1.head(26))
print(ser2.head(26))
print(ser3.head(26))
'''
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution
ser1[~ser1.isin(ser2)]
print(ser1)