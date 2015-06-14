import math
import EulerLib
import PrimeHelper
                   
def hasForm(n):
    strN = str(n)
    if(len(strN)!=19):
        return False
    for i in range(0,20,2):
        if(int(strN[i])!=(int(i/2)+1)%10):
            return False
    return True
    
#def altHasForm(n):
    #if(n<1020304050607080900 or n>1929394959697989990):
     #   return False
    #for i in range(9,-1,   
                   
def euler206():
    startN = int(math.sqrt(1020304050607080900))
    startN = 1168200000
    nLim = int(math.sqrt(1929394959697989990))+1
    currN = startN
    print(nLim-startN)
    for i in range(startN,nLim,10):
        if(i%100000==0):
            print(i)
        if(hasForm(i*i)):
            print(i)
            print(i*i)
            break

euler206()