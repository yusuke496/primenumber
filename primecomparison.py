import time
from math import sqrt

def pr(n):
    for i in range(2, int(sqrt(n)+1)) :
            if n%i==0 :
                return 0
                break
    else : return n

def delvalall(arr,val) :
    brr=[]
    for i in range(len(arr)) :
        if arr[i] != val :
            brr.append(arr[i])
        else :
            pass
    return brr

Ist=input("input I =")
N=int(Ist)
j=N

start = time.clock()
a=[2]
for i in range(3, N+1) :
    if pr(i) != 0 :
        a.append(i)
    else :
        pass
t=time.clock()-start
print(t, "sec", len(a), "primes")

a=[]
a=[i for i in range(2,j+1)]
ind1=j-2
ind2=j-2
i=0
k=1

start=time.clock()
while i in range(ind1) :
    while i+k in range(1,len(a)) :
        if a[i+k]%a[i]==0 :
            a[i+k]=1
        else :
            pass
        k=k+1
        #break
    a=delvalall(a,1)
    k=1
    i=i+1
    ind=len(a)
t=time.clock()-start
print(t, "sec", len(a), "primes")
