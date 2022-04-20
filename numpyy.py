import numpy as np
#A=np.array([[1,2,3],[4,5,6],[7,8,9]])
#B=np.array([[10,11,12], [13,14,15], [16,17,18]])
#print(A*B)

#mảng 1 chiều
C=np.array([1,2,3])
print(C)
#mảng 2 chiều
a=np.array(([(1,2,3),(5,6,7)],[(9,10,11),(1,5,7)],[(2,4,6),(10,12,14)]),dtype=int)
print(a)

#mảng 2 chiều với kích thước 5x5 và các phần tử bằng 0
d=np.zeros((5,5),dtype=int)
print(d)
print('số chiều: '+ str(d.ndim))

#mảng 3 chiều với kích thước 2x2x3
e=np.ones((3,4,5),dtype=int)
print(e)
print('số chiều: '+ str(e.ndim))

#tạo mảng với các phần tử từ 1-19 với bước nhảy cách nhau là 3
f=np.arange(1,20,3)
print(f)
print('số chiều: '+ str(f.ndim))

#tạo mảng 2 chiều với các phần tử bằng 9 kích thước 2x3
g=np.full((2,3),9)
print(g)
print(g.ndim)#Số chiều của mảng
print(g.shape)#Kích thước của mảng
print(g.size)#Số phần tử trong mảng
print(g.dtype)#Kiểu dữ liệu của phần tử trong mảng

#tạo ma trận đơn vị với kích thước là 6x6
r=np.eye(6,dtype=int)
print(r)
print(r.ndim)
print(r.shape)
print(r.size)
print(r.dtype)

#tạo ma trận với phần tử ngẫu nhiên kích thước3x4
t=np.random.random((3,4))
print(t)
print(t.ndim)#số chiều của mảng
print(t.shape)#số kích thước của mảng
print(t.size)#số phần tử của mảng
print(t.dtype)#số dữ liệu
