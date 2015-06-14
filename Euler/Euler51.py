import math
import EulerLib
import PrimeHelper

PH = PrimeHelper.PrimeHelper()

def euler51():
    currInd = 0
    currPrime = PH.getNthPrime(currInd)
    while(not checkIfEightPrimeFamily(currPrime)):
        currInd+=1
        currPrime = PH.getNthPrime(currInd)
    print("Current index: "+str(currInd))
    print("The prime: "+str(currPrime))

def checkIfEightPrimeFamily(p):
    if(p<=56003): #we know this is not the answer
        return False
    pStr = str(p)
    pDigits = [int(d) for d in pStr] 
    combs = EulerLib.combinationsWithStars(pDigits)
    for c in combs:
        if('*' in c):
            if(checkIfEightPrime(c)):
                return True
    return False

def checkIfEightPrime(comb):
    if(comb[-1]!="*" and int(comb[-1])%2==0):
        return False
    primeCount = 0
    hits = []
    for i in range(0,10):
        currTry = 0
        currStr = ""
        for d in comb:
            currStr = currStr + (str(i) if d=="*" else str(d))
        if(currStr[0]=='0'):
            continue
        currTry = int(currStr)
       # print(currTry)
        if(PH.isPrime(currTry)):
            primeCount+=1
            hits.append(currTry)
        if(primeCount>=8):
            break
    if(primeCount>=8):
        print(comb)
        print(hits)
    return primeCount>=8
        
        
