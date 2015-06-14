import PrimeHelper
import math

PrimeLib = PrimeHelper.PrimeHelper

def isSquareNumber(n):
    close = math.sqrt(n)
    down = int(close)
    up = int(close+1)
    return down*down==n or up*up==n

def gcd(a,b):
    while(a!=b):
        if(a==1 or b==1):
            return 1
        if(a>b):
           a-=b
        if(a<b):
            b-=a
    return a

def nChooseR(n,r):
    return int(math.factorial(n))/int(math.factorial(r)*math.factorial(n-r))

def naiveFactors(n):
    sqrtN = math.sqrt(n)
    facs = []
    nLeft = n
    pInd = 0
    while(nLeft>sqrtN):
        currPrime = PrimeLib.getNthPrime(pInd)
        pInd+=1
        if(currPrime==nLeft):
            break
        while(nLeft%currPrime==0 and nLeft>sqrtN):
            facs.append(currPrime)
            nLeft = int(nLeft/currPrime)
    facs.append(nLeft)
    return facs

def rationalIsLess(n1,d1,n2,d2):
    return n1*d2<d1*n2

def simpleModularExponentiation(n,e,mod):
    currModded = 1
    for i in range(1,e):
        currModded*=n
        currModded=currModded%mod
    return currModded

def combinations(nums):
	numLen = len(nums)
	pows = [int(math.pow(2,i)) for i in range(0,numLen)]
	lim = int(math.pow(2,numLen))
	combs = []
	for j in range(1,lim):
		currComb = []
		for i in range(0,numLen):
			currN = nums[i]
			currN*=(j & pows[i])
			if(currN!=0):
				currComb.append(nums[i])
		combs.append([])
		combs[-1] = currComb
	return combs

def combinationsWithStars(nums):
	numLen = len(nums)
	pows = [int(math.pow(2,i)) for i in range(0,numLen)]
	lim = int(math.pow(2,numLen))
	combs = []
	for j in range(1,lim):
		currComb = []
		for i in range(0,numLen):
			currN = nums[i]
			currN*=(j & pows[i])
			if(currN!=0):
				currComb.append(nums[i])
			else:
                                currComb.append("*")
		combs.append([])
		combs[-1] = currComb
	return combs    

def getProduct(facs):
    num = 1
    for f in facs:
        num*=f
    return num

def continuedExpansionN(continuedFrac,n):
    currN = continuedFrac[n]
    currD = 1
    for i in range(n-1,-1,-1):
        currF = continuedFrac[i]
        currN, currD = currD, currN
        currN+=int(currF*currD)
    return currN,currD
        


            
#a,b = continuedExpansionN(continuedFractionRoot2,1)
#print(str(a)+"/"+str(b))

#not needed since we know the expansion of root 2 already
def continuedFraction(d,n):
    continuedFrac = []
    currD = 0
    currEst = 0
    for i in range(0,n):
        if(currD==0):
            currEst = int(d)
            currD = d-currEst
            continuedFrac.append(currEst)
        else:
            currEst = int(1/currD)
            currD = 1/()
        #TODO
    

class Point():
    def __init__(self,x,y):
        self.X = x
        self.Y = y

    def epsilonEquals(self,point):
        epsilon = 0.001
        return(abs(self.X-point.X)<=epsilon and abs(self.Y-point.Y)<=epsilon)
    
def getPolygonalNumber(p,n):
    if(p==3):
        return int((n*(n+1))/2)
    if(p==4):
        return n*n
    if(p==5):
        return int((n*(3*n-1))/2)
    if(p==6):
        return int((n*(2*n-1)))
    if(p==7):
        return int((n*(5*n-3))/2)
    if(p==8):
        return int((n*(3*n-2)))

def smartishResilience(primeFactorsIn):
    primeFactors = []
    primeFactorsIn.sort()
    for i in primeFactorsIn:        
        if(len(primeFactors)==0 or primeFactors[-1]!=i):
            primeFactors.append(i)
    num = getProduct(primeFactorsIn)
    combs = combinations(primeFactors)
    baseDen = num-1
    currNum = baseDen
    #mod 2 =1 subtract
    #mod 2=0 add
    for currComb in combs:
        currProd = getProduct(currComb)
        currColl = int(num/currProd)-1
        if(len(currComb)%2==1):
            currNum-=currColl
        else:
            currNum+=currColl
    return currNum, baseDen, currNum/baseDen

