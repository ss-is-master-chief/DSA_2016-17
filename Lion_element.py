m=int(input("Enter number of elements in array: "))
b=[]
for i in range(m):
    e=int(input())
    b.append(e)
s=int(input("Enter element to be found: "))
mid=int(m/2)
last=len(b)-mid
x=b[:mid+1]
y=b[mid+1:]
count=0
for i in range(0,len(x)):
    if x[i]==s:
        count+=1
        if count>mid:
            continue
if count<mid:
    for i in range(0,len(y)):
        if y[i]==s:
            count+=1
            if count>mid:
                continue
if count>=mid:
    print("Lion element")
else:
    print("Not Lion element")

    

