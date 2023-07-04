import time
from math import sqrt
import matplotlib.pyplot as plt

def pr(n):
    for i in range(2, int(sqrt(n)+1)) :
            if n%i==0 :
                return 0
                break
    else : return n

Nin=input("start Number")
Nfi=input("final Number")
Ni=int(Nin)
Nf=int(Nfi)
start = time.clock()
a=[]
t=[]
start=time.clock()
for i in range(Ni, Nf+1) :
    if pr(i) != 0 and i != 1:
        #print(time.clock()-start, len(a)+1, i)
        a.append(i)
        t.append(time.clock()-start)
    else :
        pass
numprime=[i for i in range(1,len(a)+1)]
print(a)
print(len(a),t[len(t)-1])
#plt.title("Prime Number")
#plt.xlabel("Prime Number")
#plt.ylabel("number")
#plt.scatter(numprime, a, linewidth=1, color="black")
#plt.show()
