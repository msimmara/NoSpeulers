import EulerLib
import PrimeHelper
import math
import datetime


def cubeRange(n):
    nCubed = n*n*n
    strNCubed = str(nCubed)
    digCount = len(strNCubed)
    
    lowCubed = math.pow(10, digCount-1)
    highCubed = lowCubed*10 - 1
    
    lowN = int(math.pow(lowCubed, (1/3)))
    highN = int(math.pow(highCubed, (1/3)))+1
    
    return lowN, highN

def checkIfPerm(n,m):
    nStr = str(n)
    mStr = str(m)
    if(len(nStr)!=len(mStr)):
        return False
    
    nBucket = [0 for i in range(0,10)]
    mBucket = [0 for i in range(0,10)]
    
    for dig in nStr:
        intDig = int(dig)
        nBucket[intDig]+=1
        
    for dig in mStr:
        intDig = int(dig)
        mBucket[intDig]+=1
        
    for i in range(0,10):
        if(nBucket[i]!=mBucket[i]):
            return False
    
    return True

def findCubedPerms(n):
    nCubed = n*n*n
    rangeL, rangeH = cubeRange(n)
    perms = []
    for i in range(rangeL,rangeH+1):
        iCubed = i*i*i
        if(checkIfPerm(nCubed, iCubed)):
            perms.append(i)
           
    
    return perms

def euler62():
    startN = 345
    currN = startN
    mostPerms = 0
    fivePermFound = False
    while(not fivePermFound):
        currPerms = findCubedPerms(currN)
        currPermLen = len(currPerms)
        if(currPermLen>mostPerms):
            mostPerms = currPermLen
            print("New high found!")
            print(currPerms)
        if(currPermLen==5):
            fivePermFound = True
            print("Answer found!")
            print(currPerms)
        currN+=1    
    
euler62()
    
