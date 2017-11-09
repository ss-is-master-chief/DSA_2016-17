def primeexp(n):
    y=n
    import math
    fact_exp = []
    fact_exp.append([n,1])
    i=2
    for j in range(2,n):
        if n%i == 0:
            exp = 0
            while n%i == 0:
                exp+=1
                n/=i
            fact_exp.append([i,exp])
    print ('Prime Exponential Factorization of '+str(y)+ ' is -->',(fact_exp))

def factors(x):
    fact = []
    fact.append(x)
    for i in range (1,x):
        if (x%i==0):
            fact.append(i)
    print('Factors of '+ str(x) +' --> ',sorted(fact))
    print('Number of Divisors --> ',len(sorted(fact)));print('\n')


i=0 #integers over which implemented
c1=0 #counter
p=0 #previous highest number of divisors
c2=0 #counter
n=int(input("Enter how many HCNs to be generated: "))
l=[] #list to which the numbers have to be appended
for a in range(1,n+1):#To facilitate printing of each HCN till n
    while (c2<a):
        c1=j=0
        i+=1     #increments i
        while (j<i):
            j+=1;
            c1+=i%j==0 #To check
        if (c1>p):
            p=c1  #sets previous largest divisor to counter
            c2+=1 #increments counter 2
    l.append(i)
    
print('\n')
print(l)
print('\n')

for each in l:
    factors(each)
for every in l:
    primeexp(every)

        

    

        
                
                
            
        
