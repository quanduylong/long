
import pandas as pd
import numpy as np
from pandas import ExcelFile
'''
#SERIES
#TẠO SERIES KHÔNG TRUYỀN INDEX
d=pd.Series([3,2,5,4])
print(d)
#TẠO SERIES CÓ TRUYỀN INDEX
a=pd.Series([1,2,3,4],index=('a','b','c','d'))
print(a)
#TẠO SERIES TỪ DICT
b={'a':3,'b':2,'c':5,'d':2,'g':7,'t':1}
c=pd.Series(b,index=['a','b','c','d','e','f'])
print(c)

#TRUY CẬP DỮ LIỆU TỪ SERIES VỚI INDEX VÀ VỊ TRÍ
c={'q':1,'w':2,'e':3,'r':4,'t':9,'g':7}
v=pd.Series(c,index=['q','w','e','r','t','g','h'])
print(v)
print(v['q'])
print(v['e'])
print(v[:'e'])#LẤY VỊ TRÍ TỪ ĐẦU ĐẾN VỊ TRÍ INDEX CỤ THỂ 
print(v[:4])#LẤY DỮ LIỆU THEO VỊ TRÍ, 4 VỊ TRÍ ĐẦU
print(v[-3:]) #LẤY NHỮNG VỊ TRÍ TỪ VỊ TRÍ THỨ 3

#CHUYỂN ĐỔI SANG DẠNG ARRAY CỦA SERIES BẰNG NUMPY.ASARRAY
data=pd.Series([5,6,9,8,7],index=['a','b','c','d','e'])
data2={'a':1,'b':2,'c':3,'d':4,'e':5}
c=pd.Series(data2,index=['a','b','c','d','e','r'])
a=np.asarray(data)
b=np.asarray(c)
print(a)
print(b)

#DATAFRAME
#TẠO DATAFRAME TỪ DICT CÁC SERIES 1
a={'Một': pd.Series([1,2,3,5],index=['a','b','c','e']), 
'Hai': pd.Series([1,2,3,4],index=['a','b','c','d'])}
s=pd.DataFrame(a)
print(s)
#TẠO DATAFRAME TỪ DICT CÁC SERIES 2
b={'ONE': pd.Series([1,2,3,5],index=['a','b','c','e']), 'TWO': pd.Series([1,2,3,4],index=['a','b','c','d'])}
r=pd.DataFrame(b,index=['a','c','d'])
print(r)

#THAO TÁC CHỌN, THÊM, XÓA CỘT
c={'ONE': pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
    'TWO':pd.Series([7,8,9,10,11,12],index=['a','b','c','d','e','f']),
    'THREE':pd.Series([1,3,5,7,9,8],index=['a','b','c','d','e','f'])}
cc=pd.DataFrame(c)
print(cc)
#CHỌN CỘT
print(cc['THREE'])#CHỌN CỘT 3
print(cc['ONE'])#CHỌN CỘT 2
#THÊM CỘT
cc['FOUR']=cc['TWO']-cc['THREE']#THÊM CỘT FOUR VỚI GIÁ TRỊ BẰNG TWO TRỪ THREE
cc['Chuẩn']= 11#THÊM CỘT VỚI GIÁ TRỊ VÔ HƯỚNG(scalar value) 
cc['NEW']=cc['THREE'][:4]#THÊM CỘT KHÔNG CÙNG SỐ LƯỢNG INDEX VỚI DATA FRAME
cc['TRUE/FALSE']=cc['TWO']==9#THÊM CỘT TRUE/FALSE THEO ĐIỀU KIỆN
cc.insert(1,'CHÈN',cc['TWO'])#DÙNG INSERT, CỘT 'CHÈN' Ở VỊ TRÍ THỨ 1 TÍNH TỪ 0, CÓ GIÁ TRỊ BẰNG CỘT 'TWO' 
print(cc)
#XÓA CỘT 
del cc['THREE']#XÓA CỘT 'THREE'
xoa=cc.pop('ONE')#XÓA CỘT 'ONE' BẰNG HÀM pop
print(cc)
y=cc.loc['a']#CHỌN DÒNG THEO LABEL
print(y)
y=cc.iloc[4]#CHỌN DÒNG THEO VỊ TRÍ NGUYÊN
print(y)
y=cc[2:4]#CẮT DÒNG TỪ INDEX 2 DẾN 4
print(y)
'''
excel_file= 'C:\\Users\\Admin\\Downloads\\movies.xls'
movies=pd.read_excel(excel_file)
