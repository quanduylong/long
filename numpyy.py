import numpy as np
'''
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[10,11,12], [13,14,15], [16,17,18]])
print(A*B)
print ("next")
#mảng 1 chiều
C=np.array([1,2,3])
print(C)
print ("next")
#mảng 2 chiều
a=np.array(([(1,2,3),(5,6,7)],[(9,10,11),(1,5,7)],[(2,4,6),(10,12,14)]),dtype=int)
print(a)
print ("next")
#mảng 2 chiều với kích thước 5x5 và các phần tử bằng 0
d=np.zeros((5,5),dtype=int)
print(d)
print('số chiều: '+ str(d.ndim))
print ("next")
#mảng 3 chiều với kích thước 2x2x3
e=np.ones((3,4,5),dtype=int) 
print(e)
print('số chiều: '+ str(e.ndim))
print ("next")
#Tạo mảng với các phần tử từ 1-19 với bước nhảy cách nhau là 3
f=np.arange(1,20,3)
print(f)
print('số chiều: '+ str(f.ndim))
print ("next")
#Tạo mảng 2 chiều với các phần tử bằng 9 kích thước 2x3
g=np.full((2,3),9)
print(g)
print(g.ndim)#Số chiều của mảng
print(g.shape)#Kích thước của mảng
print(g.size)#Số phần tử trong mảng
print(g.dtype)#Kiểu dữ liệu của phần tử trong mảng
print ("next")
#Tạo ma trận đơn vị với kích thước là 6x6
r=np.eye(6,dtype=int)
print(r)
print(r.ndim)
print(r.shape)
print(r.size)
print(r.dtype)
print ("next")
#tạo ma trận với phần tử ngẫu nhiên kích thước3x4
t=np.random.random((3,4))
print(t)
print(t.ndim)#số chiều của mảng
print(t.shape)#số kích thước của mảng
print(t.size)#số phần tử của mảng
print(t.dtype)#số dữ liệu
print ("next")
#Nhân ma trận này với ma trận khác
A = np.array([[1, 3, 4], [-2, 6, 0], [-5, 7, 2]])
B = np.array([[2, 3, 4], [-1, -2, -3], [0, 4, -4]])
print("A * B = \n", A.dot(B))# hoặc A@B hoặc np.dot(A,B)
print("B * A = \n", B.dot(A))# hoặc B@A hoặc np.dot(B,A)
print ("next")
#Ma trận đường chéo
u=np.diag([4,5,6])
print(u)
#Lấy đường chéo chính trên một ma trận
o=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.diag(o))
print ("next")
#Ma trận chuyển vị
i=np.array([[2,5,1],[7,6,8],[6,1,8]])
print(np.transpose(i))
#or
print(i.T)
print ("next")
#Định thức ma trận vuông
y=np.array([[4,5,6],[55,3,2],[15,4,3]])
print(np.linalg.det(y))
print ("next")

#Ma trận nghịch đảo
v=np.array([[2,5,6],[6,7,8],[6,88,9]],dtype=int)
print(np.linalg.inv(v))

#Cách lấy cột trong ma trận
A = np.array([[1, 4, 5, 12], 
 [-2, 8, 6, 14],
 [-1, 5, 10, 22]])

print("A[:,0] =",A[:,0]) # Cột đầu tiên
print("A[:,3] =", A[:,3]) # Cột thứ 4
print("A[:,-1] =", A[:,-1]) # Cột cuối cùng (Cột thứ 4)

#NỐI MA TRẬN NÀY VS MA TRẬN KHÁC
A = np.array([[1,20,4],[5,6,8], [15,2,8]])
B = np.array([[10,11,12],[6,8,4]])
C= (B.T)
print('Nối C và A tạo thành shape 3x5\n',np.concatenate((C,A),axis=1))
'''
print("*MA TRẬN NÂNG CAO*")
#thay đổi kích thước ma trận với Reshape
print('chuyển từ 1 chiều sang 2')
s=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(s.reshape(3,4))
print('chuyển từ 2 chiều sang 1')
p=np.array(([1,2,3],[4,5,6],[7,8,9]))
print(s.reshape(-1))
print('thay đổi số hàng số cột')
w=np.array([[1,2,3],[4,5,6],[7,8,9],[13,14,15]])
print(w.reshape(3,4))
print('hạng của ma trận')
k=np.array([[-2,1,0,2,3,-1],[4,2,-1,0,-2,1],[6,5,-2,2,-1,1],[-6,-1,1,2,5,-2]])
print(np.linalg.matrix_rank(k))
print('Vết của ma trận (trace) là tổng của đường chéo chính')
h=np.array([[1,5,6],[2,5,8],[6,5,8]])
print(np.trace(h))
#or
print(h.trace())
print('*CHUẨN CỦA MA TRẬN')
n=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print('theo hàng')
print(np.linalg.norm(n,ord=np.inf)) #Chuẩn theo hàng
print('theo cột')
print(np.linalg.norm(n,ord=1)) #Chuẩn theo cột
print('theo Froebenius')
print(np.linalg.norm(n))# Chuẩn theo Euclide-hay còn gọi là  Frobenius
import math as mt
print(mt.sqrt(np.trace(np.transpose(n)@ n)))#or công thức theo vết tính Frobenius
#or
print(mt.sqrt(np.trace(n.T@n)))
print('*TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN')
v=np.array([[2,1,0],[1,3,1],[0,1,2]])
j,h = np.linalg.eig(v)
print('Eigenvalue(Trị riêng):\n',j)
print('Eigenvectors(Vector riêng):\n',h)  
print('Các hàm thao tác trên ma trận') 
t=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(t))#Tổng các phân tử của ma trận
print(np.sum(t,axis=0))#Tổng các phân tử trên cột
print(np.sum(t,axis=1))#Tổng các phần tử trên hàng 
print(np.mean(t))#Trung bình tổng ma trận
print(np.mean(t,axis=0))#Trung bình tổng trên cột
print(np.mean(t,axis=1))#Trung bình tổng trên hàng 

#NHAP MA TRAN
mt=[[],[],[]]
def NhapMaTran():
    for i in range(l):
        for j in range(c):
            print ("Phan tu hang",i,"cot",j)
            pt=int(input(""))
            mt[i].append(pt)

def InCheoChinh():
    print ("Duong cheo chinh cua ma tran vua nhap la:")
    for i in range(l):
        for j in range(c):
            if i!=j:
                mt[i][j]="*"
    for i in range(l):
        for j in range(c):
            print (mt[i][j],'   ',mt[i][j+1],'  ',mt[i][j+2])
            break        
print ("MENU\n1.Chon 1 de Nhap vao ma tran.")
print ("2. Chon 2 de In cac phan tu duong cheo chinh.")
print ("3. Chon 3 de Ket thuc.\tMoi ban chon")
ch=0
while ch!=3:
    ch=int(input("CHON:"))
    if ch==1:
        l=int(input("Nhap so hang:"))
        c=int(input("Nhap so cot:"))
        NhapMaTran()
    elif ch==2:
        InCheoChinh()
    else:
        print("Chon khong hop le, moi chon lai!")
        main()    