import multiprocessing
from joblib import Parallel, delayed
import time
import numpy as np
from math import sqrt

#corenum=multiprocessing.cpu_count()
#core=int(corenum/2)

#def delvalall(arr,val) :
#    brr=[]
#    for i in range(len(arr)) :
#        if arr[i] != val :
#            brr.append(arr[i])
#            pass
#    return brr

def pr(n):
    for i in range(2, int(sqrt(n)+1)) :
            if n%i==0 :
                return 0
                break
    else : return n

if __name__=='__main__' :
    Ist=input("input I: ")
    NumCore=input("input number of cores: ")
    j=int(Ist)
    core=int(NumCore)
    #core=multiprocessing.cpu_count()
    start = time.clock()
    result = Parallel(n_jobs=core)(delayed(pr)(k) for k in range(2, j+1))
    result=np.sort(result)
    result=np.trim_zeros(result)
#   result = delvalall(result,0)
    t=time.clock()-start
    print(result)
    print(t,"sec",core,"cores",len(result),"primes")
