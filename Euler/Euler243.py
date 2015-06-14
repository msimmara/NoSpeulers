import math

RTB_n = 15499
RTB_d = 94744
RTB_approx = RTB_n/RTB_d

primeList = [2,3]
primeCount = 2
primeListUpperBound = 3

def isPrime(n):
    rootN = math.sqrt(n)
    if(primeListUpperBound<rootN):
        updatePrimes(rootN)
    currP = 0
    currInd = 0
    while(currP<rootN and currInd<primeCount):
        currP = primeList[currInd]
        if(n%currP==0):
            return False
        currInd+=1
    return True

def updatePrimes(upperBound):
    global primeListUpperBound
    global primeCount
    while(primeListUpperBound<upperBound):
        primeListUpperBound+=2
        if(isPrime(primeListUpperBound)):
            primeList.append(primeListUpperBound)
            primeCount+=1

def gcd(a,b):
    while(a!=b):
        if(a==1 or b==1):
            return 1
        if(a>b):
           a-=b
        if(a<b):
            b-=a
    return a

def checkAnswer(candidateNum,candidateDen):
    return candidateNum*RTB_d<candidateDen*RTB_n

#assuming d>1
def naiveResilience(d):
    den = d-1
    resilientCount = 1 #1 is always resilient
    if(isPrime(d)):
        return d-1,d-1, 1
    for i in range(2,d):
        if(gcd(i,d)==1):
            resilientCount+=1
    return resilientCount, den, resilientCount/den

def naive243():
    currentD = 3
    correct = False
    while(not correct):
        currResN, currResD,currResApp = naiveResilience(currentD)
        correct = checkAnswer(currResN, currResD)
        currentD+=1
        if(currentD%1000==0):
            print(currentD)            
    print(currentD)
    return currentD

def naiveFactors(n):
    sqrtN = math.sqrt(n)
    updatePrimes(sqrtN)
    facs = []
    nLeft = n
    pInd = 0
    while(nLeft>sqrtN):
        currPrime = primeList[pInd]
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

def naiveInvestigate(n):
    lowestN=1
    lowestD=1
    for i in range(2,n):
        x,y,z = naiveResilience(i)
        if(rationalIsLess(x,y,lowestN,lowestD)):
            lowestN=x
            lowestD=y
            facs = naiveFactors(i)
            print(str(i)+":\t\t "+str(x)+"/"+str(y)+"\t\t"+str(facs))

def somethingishInvestigate(n):
    updatePrimes(n)
    lowestN=1
    lowestD=1
    curr=2*3
    currPrime = 3
    currPrimeInd = 1
    currFacs=[2,3]
    while(curr<n):
        currPrimeInd +=1
        if(currPrimeInd>=len(primeList)):
            print(currPrimeInd)
            print(len(primeList))
            break
        currPrime = primeList[currPrimeInd]
        curr*=currPrime
        currFacs.append(currPrime)
        x,y,z = naiveResilience(curr)
        if(rationalIsLess(x,y,lowestN,lowestD)):
            lowestN=x
            lowestD=y
            possibleWinner = rationalIsLess(x,y,RTB_n,RTB_d)
            print(str(curr)+":\t\t "+str(x)+"/"+str(y)+"\t\t"+str(currFacs)+"\t\t"+("Bingo" if possibleWinner else "Nope"))
            if(possibleWinner):
                return curr
        

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

def getProduct(facs):
    num = 1
    for f in facs:
        num*=f
    return num
    
def listThoseNums(facs):
    num = getProduct(facs)
    print("N: "+str(num))
    combs = combinations(facs)
    for currentComb in combs:
        currProd = getProduct(currentComb)
        currColl = int(num/currProd)-1
        print(str(currentComb)+":\t"+str(currColl))

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

def smartishInvestigate(n):
    updatePrimes(math.sqrt(n))
    lowestN=1
    lowestD=1
    curr=2*3
    currPrime = 3
    currPrimeInd = 1
    currFacs=[2,3]
    while(curr<n):
        currPrimeInd +=1
        if(currPrimeInd>=len(primeList)):
            print(currPrimeInd)
            print(len(primeList))
            break
        currPrime = primeList[currPrimeInd]
        curr*=currPrime
        currFacs.append(currPrime)
        x,y,z = smartishResilience(currFacs)
        if(rationalIsLess(x,y,lowestN,lowestD)):
            lowestN=x
            lowestD=y
            possibleWinner = rationalIsLess(x,y,RTB_n,RTB_d)
            print(str(curr)+":\t\t "+str(x)+"/"+str(y)+"\t\t"+str(currFacs)+"\t\t"+("Bingo" if possibleWinner else "Nope"))
            if(possibleWinner):
                return curr   
