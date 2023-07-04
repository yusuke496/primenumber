import matplotlib.pyplot as plt
import time
from math import sqrt


#corenum=multiprocessing.cpu_count()
#core=int(corenum/2)

Ist=input("input I=")
j=int(Ist)
a=[i for i in range(2,j+1)]
ind1=j-2
ind2=j-2
i=0
k=1

def quicksort(x):
    if x==[]: return []
    smallerSorted = quicksort([a for a in x[1:] if a <= x[0]])
    biggerSorted = quicksort([a for a in x[1:] if a > x[0]])
    return(smallerSorted+[x[0]]+biggerSorted)

def delvalall(arr,val) :
    brr=[]
    for i in range(len(arr)) :
        if arr[i] != val :
            brr.append(arr[i])
        else :
            pass
    return brr
start=time.clock()
while i in range(ind1) :
    while i+k in range(1,len(a)) :
        if a[i+k]%a[i]==0 :
            a[i+k]=1
        else :
            pass
        k=k+1
        #break
    #a=quicksort(a)    
    a=delvalall(a,1)
    k=1
    i=i+1
    ind=len(a)
t=time.clock()-start
print(len(a),t)
num=[i for i in range(1,len(a)+1)]
plt.title("Nth prime number")
plt.xlabel("N")
plt.ylabel("prime number")
plt.scatter(num, a, linewidth=1, color="black", marker="x")
plt.show()
