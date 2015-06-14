import math
import EulerLib
import PrimeHelper
from EulerLib import smartishResilience

ph = PrimeHelper.PrimeHelper()
#ph.updatePrimesToBound(1000001)

def totient(facs):
    x,y,z = EulerLib.smartishResilience(facs)
    return x

def euler69():
    bound = 1000000
    numSeen = [False for i in range(0,bound+1)]
    ph.updatePrimesToBound(bound+1)
    print("primes primed")
    max = ph.PrimeCount+1
    maxLen = int(math.log(bound+1,2))    
    cursorLen=0    
    counter=0
    underBoundCounter = 0
    prods = []
    maxAnswer = 0
    while(cursorLen<maxLen):
        cursorLen+=1
        cursors, maxes = initializeCursorsAndMaxes(cursorLen,max)
        nProd = 0
        firstRunThrough = True
        #if(cursorLen==maxLen):
            #maxes = [1 for i in range(0,cursorLen)]
            #maxes[0]=2
        while(firstRunThrough or updateCursors(cursors, maxes)):
            firstRunThrough = False
            counter+=1
            facs = [ph.getNthPrime(n) for n in cursors]
            nProd = EulerLib.getProduct(facs)
            if(nProd<=bound):
                underBoundCounter+=1
                #print(facs)
                #prods.append(nProd)
                #numSeen[nProd]=True
                print(nProd)
                currTotient = totient(facs)
                if((nProd/currTotient)>maxAnswer):
                    maxAnswer = nProd/currTotient
                    print("Max found")
                    print(maxAnswer)
                    print(nProd)
                
                
    
    #print(counter)
    #print(underBoundCounter)
    #print(numSeen)

#TODO add nProd max?
def initializeCursorsAndMaxes(n,max):
    cursors = [1 for i in range(0,n)]
    maxes = [max for j in range(0,n)]
    return (cursors,maxes)

def updateCursors(cursors,maxes):
    cLen = len(cursors)
    maxedOn = -1
    #debCurs = [c for c in cursors]
    for i in range(cLen-1,-1,-1):
        if(cursors[i]<maxes[i]):
            cursors[i]+=1
            maxedOn = i            
            break
    if(maxedOn==-1):
        #print("Maxed on -1")
        #print(cursors)
        return False
    
    upC = cursors[maxedOn]
    for j in range(maxedOn+1,cLen):
        upC+=1
        cursors[j] = 1
        
    for i in range(cLen-1,-1,-1):
        if(cursors[i]>maxes[i]):
            #print("Maxed on")
            #print(debCurs)
            #print(cursors)
            #print(maxes)
            return False
    
    return True

#euler69()
def calcMaxes(bound,len):
    curr= 1
    count =1
    maxes = []
    while(curr<bound):
        count+=1
        curr=ph.getNthPrime(count)
    
    maxes.append(count)
    