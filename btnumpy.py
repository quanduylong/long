import math
import random
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
'''

#TODO5
m=int(input('So hoc sinh: '))
for i in range(1,m+1):
    while x<8:
        x=random.randint(-10,10)

    print(i)

