import pandas as pd
a=pd.Series([1,2,3,4],index=('a','b','c','d'))
print(a)

b={'a': -1.3, 'b':11.7,'d':2.0,'f':10,'g':5}
c=pd.Series(b,index=['a','b','c','d','e','f'])
print(c)