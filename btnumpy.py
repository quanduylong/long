
import math
import random
from re import I
import numpy as np

'''
#TODO1

m=int(input('Nhập số nguyên m: '))
n=int(input('Nhập số nguyên n: '))
l=int(input('Nhập số nguyên l: '))
a=np.array([2.5,3,9,10,11,6.72,4.5,0,35,10,67,23])
b=np.array([1,2,3,4,5,6])
A=a.reshape(m,n)
B=b.reshape(n,l)
print ('A*B= ', A@B)

#TODO2

m=2
n=3
a=np.array([3,4,2,-3.3,2,3])
b=np.array([12,-2.42,32.3,32,-193,22.3])
A=a.reshape(m,n)
B=b.reshape(m,n)
print('A+B=\n',A+B)
print('A-B=\n',A-B)


#TODO3

m=int(input('Nhập số nguyên m: '))
n=int(input('Nhập số nguyên n: '))
t= m*n
a=np.arange(1,13)
A=a.reshape(m,n)
print(np.sum(A,axis=0))


#TODO4
A=np.array([[4, 5, 2], [11, 15, 3]])
B=np.array([[2, 7, 14], [4, 15, 26], [7, 8, 9], [10, 11, 12]])
C=np.array([[5, 16], [17, 3], [29, 1], [1, 2]])
x=np.array([[4, 15],[16, 17]])
d=(A@B.T) #OR np.transpose(d)
y=C.T#or np.transpose(C)
Y=x@(d+y)
print(Y)


#TODO5
m=int(input('So hoc sinh: '))
l=np.array([1,2,3,4,5,6,7])
t=np.array([2.2,5,3,6,7,8,9])
c=np.array([5,6,8,4,2,3,5]) 
A=np.array([-1,3,7,9,6,1,2])
tvh=A@l,A@t,A@c
print('Học sinh có tính cách giống A nhất: '+str(np.max(tvh)))

#TODO6
m=int(input('Nhập số nguyên m: '))
n=int(input('Nhập số nguyên n: '))
A=np.random.randint(1,10,(m,n))
        print(np.max(A,axis=0))

#TODO7
A=np.array([[1, 2, 3], [4, 5, 6]])
B=np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
C=np.array([[-5, -6], [-7, -8], [-9, -10], [-11, -12]])
x=np.array([4, 5, 6, 7])
Y=(A@(B.T)+(C.T))**2@x+2*A@(A-(B.T)@x).T
print(Y)    

#TODO12
A =np.array([[-1, 3, 2, -2],[-5, 41, 24, -2],[0, 7, 3, 15]])
B =np.array([[1, 13, 1, 2],[15, 1, 2, 2],[10, 2, 2, 1]])    
C= A@(B.T)
D=np.sum(np.min(C,axis=1))
E=np.sum(np.max(C,axis=0))
print(D)
print(E)

#TODO11
A=np.array([[5,5,10,9,5],[4,29,18,-4.5,3],[5,19,-8,4.5,13],[19,-9,28,4.5,3],[9,9,4,3,4]])
print(A)
print('Các phần tử lớn nhất trên từng cột của ma trận A nhưng không tính biên của ma trận A là:')
print(np.max(A[:,1][1:3]))
print(np.max(A[:,2][1:3]))
print(np.max(A[:,3][1:3]))

#TODO14
A = np.array([[1,20,4],[5,6,8], [15,2,8]])
B = np.array([[10,11,12],[6,8,4]])
C= (B.T)
print('Nối C và A tạo thành shape 3x5\n',np.concatenate((C,A),axis=1))

#TODO15
a = np.array([5,4,12,13,9,14])
b = np.array([1,4,42,13,9,1])
for i in a:
    for y in b:
        if i==y:
            print(i,end=',')
'''           
#TODO16
n=int(input())
m=int(input())
A=np.arange(n,m+1)
print(np.where(A%2==0,A,0))



