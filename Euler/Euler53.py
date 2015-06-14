import EulerLib
import math

def checkNCRCountOverX(n,x):
    r = int(n/2)
    ct = 0
    while(r>=0):
        curr = EulerLib.nChooseR(n,r)
        if(curr>x):
            ct+=1
            r-=1
        else:
            break
    ct*=2
    if(n%2==0): ct-=1
    return ct
        

def euler53():
    initialN = 23
    countOverAMill = 0
    for n in range(initialN,101):
        countOverAMill+=checkNCRCountOverX(n,1000000)
    print(countOverAMill)
