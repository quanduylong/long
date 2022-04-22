''''
number=int(input("Nhập số: "))
for a in range(0,number):
    x=2**a
    if x<1025:
        print('2^%d=%d' %(a,x))
    else:
        print(str(x)+"Lớn hơn 1025 => Sai")

def bangcuuchuong(a):
    print('Bảng cửu chương số '+ str(a))
    for i in range(10):
        t=a*i
        print('%d*%d=%d' %(a,i,t))
    return 
print(bangcuuchuong(9))



A =[0,1,2,3,4,5]
def avgArray():
    for x in A:
        y = (A[0] + A[1] + A[2] + A[3] + A[4])/5
        A[x]=y
        print(y)
        return y
avgArray()



import numpy as np
import math
X = np.array([0, 30, 45, 60, 90, 120, 130, 145], dtype = int)
Y = np.zeros(shape = (X.size))
Z = np.zeros(shape = (X.size))
for i in range(0, X.size, 1):
    Y[i] = math.pi/2 - X[i]
    Z[i] = math.cos(X[i]) + math.sin(X[i])
print(X)
print("\n")
print(Y)
print("\n")
print(Z)
print("\n")
print("Tong Z: ", np.sum(Z))
'''

