n=int(input("Enter order of matrix : "))
a=[]
b=[]

def enter(x):
      if n%2==0:
            for i in range(0,n):
                  ini=[]
                  for j in range(0,n):
                        e=int(input())
                        ini.append(e)
                  x.append(ini)
      else:
            for i in range(0,n):
                  ini=[]
                  for j in range(0,n):
                        e=int(input())
                        ini.append(e)
                  ini.append(0)
                  x.append(ini)
            zero=[]
            for i in range(0,n+1,1):
                  zero.append(0)
            x.append(zero)      
      
def append(x,m,hs,he,vs,ve):
      for i in range(vs,ve):
            ini=[]
            for j in range(hs,he):
                  ini.append(x[i][j])
            m.append(ini)

def addmat(mat1,mat2):
      mat=[]
      for i in range(0,len(mat1)):
            ini=[]
            for j in range(0,len(mat1)):
                  ini.append(mat1[i][j]+mat2[i][j])
            mat.append(ini)
      return mat            

def submat(mat1,mat2):
      mat=[]
      for i in range(0,len(mat1)):
            ini=[]
            for j in range(0,len(mat1)):
                  ini.append(mat1[i][j]-mat2[i][j])
            mat.append(ini)      
      return mat            
      
def mulmat(mat1,mat2):
      mat=[]
      for i in range(0,len(mat1)):
            ini=[]
            for j in range(0,len(mat1)):
                  ini.append(0)
            mat.append(ini)      
      for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                  for k in range(len(mat2)):
                        mat[i][j]+=mat1[i][k]*mat2[k][j]
      return mat			
                  
print("Enter elements of matrix A row-wise")
enter(a)
print("Enter elements of matrix B row-wise")
enter(b)

a11=[]
a12=[]
a21=[]
a22=[]
append(a,a11,0,len(a)//2,0,len(a)//2)
append(a,a12,len(a)//2,len(a),0,len(a)//2)
append(a,a21,0,len(a)//2,len(a)//2,len(a))
append(a,a22,len(a)//2,len(a),len(a)//2,len(a))

b11=[]
b12=[]
b21=[]
b22=[]
append(b,b11,0,len(b)//2,0,len(b)//2)
append(b,b12,len(b)//2,len(b),0,len(b)//2)
append(b,b21,0,len(b)//2,len(b)//2,len(b))
append(b,b22,len(b)//2,len(b),len(b)//2,len(b))


m1=mulmat(addmat(a11,a22),addmat(b11,b22))
m2=mulmat(addmat(a21,a22),b11)
m3=mulmat(a11,submat(b12,b22))
m4=mulmat(a22,submat(b21,b11))
m5=mulmat(addmat(a11,a12),b22)
m6=mulmat(submat(a21,a11),addmat(b11,b12))
m7=mulmat(submat(a12,a22),addmat(b21,b22))
c11=submat(addmat(addmat(m1,m4),m7),m5)
c12=addmat(m3,m5)
c21=addmat(m2,m4)
c22=submat(addmat(addmat(m1,m3),m6),m2)

for i in range(0,len(c11)):
      print(c11[i],c12[i])
for i in range(0,len(c21)):
      print(c21[i],c22[i])


     
            
