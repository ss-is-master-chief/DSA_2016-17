def chain_order(p,n):
    m=[[0 for x in range(n)] for x in range(n)]
    s=[[0 for x in range(n)] for x in range(n)]
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            m[i][j]=float('inf')
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q<m[i][j]:
                    m[i][j]=q
                    s[i][j]=k
    return (m,s)

def optimal(s,i,j):
    if i==j:
        print("A",i)
    else:
        print(optimal(s,i,s[i][j]),optimal(s,s[i][j]+1,j))

p=[30,35,15,5,10,20,25]
n=len(p)
m,s=chain_order(p,n)
cost=m[1][n-1]

print("Input:",p)
print("\nm:")
for i in range(1,n-1):
    for j in range(1,n):
        print("\t",m[i][j])

print("\ns: ")

for i in range(1,n-1):
    for j in range(1,n):
        print("\t",s[i][j])

print("\nOptimal Paranthesis: ")
optimal(s,1,n-1)
print("\nTotal multiplication is:",cost)
