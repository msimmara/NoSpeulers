import math
import datetime

def isNotPrime(n,candidateList):
    root = math.sqrt(n)
    for c in candidateList:
        if(n%c==0):
            return True
        if(c>root): break
    return False

def isPrime(n,candidateList):
    root = math.sqrt(n)+1
    for c in candidateList:
        if(n%c==0):
            return False
        if(c>root): break
    return True

def primesList(n,currentPrimes):
    result = currentPrimes
    lastN = 0;
    if(len(currentPrimes)>0): lastN = currentPrimes[-1]
    if(lastN>=n): return result
    if(n<2): return result
    if(lastN<2):
        result.append(2)
        lastN = 2
    if(n<3): return result
    if(lastN<3):
        result.append(3)
        lastN = 3
    currN = lastN
    while(currN<n):
        if((isPrime(currN,result)==True)):
            result.append(currN)
        currN+=2
    
    return result

def doublePrimeBound(currentPrimeList):
    if(len(currentPrimeList)==0): return primesList(1000,list())
    lastN = currentPrimeList[-1]
    return primesList(lastN*2,list())


currPrimes = primesList(10,list())

print("Primes primed")

def leftTruncate(n):
    return int(str(n)[1:])

def rightTruncate(n):
    return int(str(n)[:-1])

def isLeftTruncatablePrime(n):
    global currPrimes
    if(n>currPrimes[-1]): currPrimes = doublePrimeBound(currPrimes)
    currentN = n
    while(currentN in currPrimes):
        if(currentN<10):return True
        currentN = leftTruncate(currentN)
    return False

def isRightTruncatablePrime(n):
    global currPrimes
    while(n>currPrimes[-1]):
        currPrimes = doublePrimeBound(currPrimes)
    currentN = n
    while(currentN in currPrimes):
        if(currentN<10):return True
        currentN = rightTruncate(currentN)
    return False
    
def euler37():
    global currPrimes
    currIndex = 0
    matches = 0
    currentResults = list()
    while(matches<11):
        
        if(currIndex>=len(currPrimes)):
            currPrimes=doublePrimeBound(currPrimes)    
        currentN = currPrimes[currIndex]
        if(currentN>10):
            isR = isRightTruncatablePrime(currentN)
            isL = isLeftTruncatablePrime(currentN)
            if(isR and isL):
                print('Match!')
                print(str(currentN))
                matches+=1
                currentResults.append(currentN)
        currIndex+=1


def isNPandigital(number):
    tempNumb = str(number)
    n = len(tempNumb)
    nums = [(0 if i<n else -1) for i in range(0,10)]
    hits = 0
    for dig in tempNumb:
        digInd = int(dig)-1
        if(digInd==-1 or nums[digInd]!=0): return False
        nums[digInd] = 1
        hits+=1
    return hits==n

def moveCharBack(character,arr):
    idx = arr.index(character)
    idx2 = idx-1
    arr[idx], arr[idx2] = arr[idx2], arr[idx]

def arrToInt(arr):
    someString = ''
    for a in arr:
        someString+=a
    return int(someString)

def getNPandigitals(n):
    nums = [str(i) for i in range(1,n+1)]
    numsCopy = nums[:]
    results = list()
    results.append(arrToInt(nums[:]))
    if(n==1): return results
    nC = n+1
    while(nums!=numsCopy or len(results)==1):
        if(nC==1): break
        nC-=1
        charToMove = str(nC)
        while(nums.index(charToMove)!=0):
            moveCharBack(charToMove,nums)
            if(nums!=numsCopy): results.append(arrToInt(nums[:]))

    return results

NPandigitals = [[],[1]]

def setUpNPandigitals(n):    
    global NPandigitals
    if(len(NPandigitals)>=(n+1) or n==1): return
    print ('Need to set up for ' +str(n-1))
    setUpNPandigitals(n-1)
    print('Just set up for ' +str(n-1))
    lastPans = NPandigitals[n-1]
    currentList = list()
    for pan in lastPans:
        for nIndex in range(0,n+1):
            panStr = str(pan)
            newArr = panStr[:nIndex]
            newArr+=str(n)
            newArr+= panStr[nIndex:]
            newPan = arrToInt(newArr)
            currentList.append(newPan)
    NPandigitals.append(currentList)
   

highestPrimePan = 0;

def concatTest(factor, n):
	result = ''
	for i in range(1,n+1):
		result+=str(i*factor)
	return int(result)

def findMaxFactorForN(n):
    currFactor = 1
    while(concatTest(currFactor+1, n)<1000000000):
        currFactor+=1
    return currFactor

def findMaxNForFactor(factor):
    if(factor==1): return 999999999
    currN=1
    for i in range(1,10):
        if(concatTest(factor,i)>1000000000):
            return i-1
    return 9

def findHighest9PandigitalForN(n):
    setUpNPandigitals(9)
    maxFactor = findMaxFactorForN(n)
    currentBest = 0
    for i in range(maxFactor+1,0,-1):
        curr = concatTest(i,n)
        if(curr in (NPandigitals[9])):
            print(curr)
            return curr
        
def is38ConcatWithFactor(n,factor):
    for i in range(1,10):
        curr = concatTest(factor,i)
        if(curr==n): return True
    return False

def is38Concat(n):
    nStr=str(n)
    for i in range(1,9):
        currFactor = arrToInt(nStr[:i])
        if(is38ConcatWithFactor(n,currFactor)):
            return True
    return False
        
    

def euler38():
    highestConcatPan = 0
    setUpNPandigitals(9)
    print ('NPanDigitals Loaded')
    ninePans = NPandigitals[9]
    for pan in ninePans:
        if(pan>highestConcatPan and is38Concat(pan)):
            highestConcatPan = pan
    print(highestConcatPan)

def euler41():
    global highestPrimePan
    setUpNPandigitals(9)
    print ('NPanDigitals Loaded')
    nPans = NPandigitals
    print ('nPans Loaded')
    for currPanList in nPans:
        for currentPan in currPanList:
            if(currentPan>highestPrimePan and (isPrime(currentPan,currPrimes))):
                highestPrimePan = currentPan

    print(highestPrimePan)

def getMultiples(n,lowerBound, upperBound):
    ct = 0
    results = list()
    current = -1
    while(current<upperBound):
        ct+=1
        current = n * ct
        if(current>lowerBound and current<upperBound):
            results.append(current)
    return results

def removeWithRepeating(numList):
    result = list()
    for i in numList:
        temp = [False for i in range(0,11)]
        tempNumStr = str(i)
        add = True
        for dig in tempNumStr:
            if(temp[int(dig)]):
                add = False
                break
            temp[int(dig)] = True
        if(add): result.append(i)
    return result

def concatAll(numList1, numList2):
    results = list()
    for num1 in numList1:
        num1Str = str(num1)
        if(len(num1Str)==2): num1Str = '0'+num1Str
        if(len(num1Str)<3): continue
        for num2 in numList2:
            num2Str = str(num2)
            if(len(num2Str)==2): num2Str = '0'+num2Str
            if(len(num2Str)<3): continue
            results.append(int(num1Str+num2Str))
    return results

def getMissingDigits(numStr):
    result = [str(i) for i in range(0,10)]
    for dig in numStr:
        if(dig not in result):
            print('sumpin weird')
            print(numStr)
        result.remove(dig)
    return result

def getPerms(chars):
    setUpNPandigitals(8)
    results = list()
    charsLen = len(chars)
    panList = NPandigitals[charsLen]
    for order in panList:
        nxt = ''
        for i in str(order):
            ind = int(i)-1
            nxt+=chars[ind]
        results.append(nxt)
    
    return results

def has43Property(candidate):
    return(int(candidate[1:4])%2==0
       and int(candidate[2:5])%3==0
       and int(candidate[3:6])%5==0
       and int(candidate[4:7])%7==0
       and int(candidate[5:8])%11==0
       and int(candidate[6:9])%13==0 and int(candidate[7:10])%17==0)
    
       

def euler43():
    results = list()
    seventeens = getMultiples(17,10,1000)
    sevens = getMultiples(7,10,1000)
    filteredSeventeens = removeWithRepeating(seventeens)
    filteredSevens = removeWithRepeating(sevens)
    combo = concatAll(filteredSevens,filteredSeventeens)
    comboFilter = removeWithRepeating(combo)
    for i in comboFilter:
        strI = str(i)
        if(len(strI)==5 and '0' not in strI): strI = '0'+strI
        if(len(strI)!=6): continue
        missingDigits = getMissingDigits(strI)
        perms = getPerms(missingDigits)
        for p in perms:
            if (int(p)%2==0):
                candidate = str(p)+str(i)
                if(has43Property(candidate)): results.append(candidate)

    return results

def isSquare(num):
    sq = math.sqrt(int(num))
    intSq = int(sq)
    return (intSq*intSq==num)

def isGold46(n,show):
    global currPrimes
    currPrimes = primesList(n+1,currPrimes)
    if(n in currPrimes):
        print(str(n)+' is prime')
        return True
    for p in currPrimes:
        if(p>n): break
        candidate = n - p
        if ((candidate%2)==1): continue
        candidate = int(candidate//2)
        if(isSquare(candidate)):
            if(show):
                sq = int(math.sqrt(candidate))
                print(str(n)+' = '+str(p)+' + 2*'+str(sq)+'^2')
            return True
    print('None for '+str(n))
    return False

def euler46():
    oddComp = 3
    while(isGold46(oddComp,False)):
        oddComp +=2
    print(oddComp)

def getPentagonalNum(i):
    return (i*((3*i)-1))//2

def test44(n1,n2):
    if(n1==n2): return False
    pent1 = getPentagonalNum(n1)
    pent2 = getPentagonalNum(n2)
    pSum = pent1+pent2
    pDiff = pent1-pent2 if (pent1>pent2) else pent2-pent1
    if(isPentagonal(pSum) and isPentagonal(pDiff)):
        print('That\'s a bingo!')
        print('pent1: '+str(pent1))
        print('pent2: '+str(pent2))
        print('n1: '+str(n1))
        print('n2: '+str(n2))
        print('Sum: '+str(pSum))
        print('Diff: '+str(pDiff))
        return True
    return False

def euler44():
    start = 0
    bingo = False
    while (not bingo):
        start+=1
        b = 1
        for i in range(start,0,-3):
            bingo = test44(i,b)
            if(bingo): break
            b+=1

def testTime(func,n):
    startT = datetime.datetime.now()
    for i in range(0,n):
        func()
    endT = datetime.datetime.now()
    totalTime = endT-startT
    avgTime = totalTime/n
    print('Total time: '+str(totalTime))
    print('Avg time: '+str(avgTime))

def isPentagonal(num):
    lowerBound = int(math.sqrt((2/3)*num))
    lowerBoundMod = lowerBound%3
    numDub = 2*num
    numDubMod = numDub%3
    nDubRoot = int(math.sqrt(numDub))+1
    for i in range((lowerBound-lowerBoundMod)-numDubMod,nDubRoot,3):
        nPent = (i*((3*i)-1))//2
        if(nPent>num): return False
        if(nPent==num): return True
    return False

def isHexagonal(num):
    lowerBound = int(math.sqrt(num/2))
    upperBound = int(math.sqrt(num))
    for i in range(lowerBound,upperBound,1):
        nHex = (i*((2*i)-1))
        if(num==nHex): return True
    return False

def test45(triangleN):
    tri = triangleN*(triangleN+1)//2
    if(isPentagonal(tri) and isHexagonal(tri)):
        print('That\'s a bingo!')
        print(tri)
        return True

def euler45():
    bingo = False
    curr = 40755
    while(not bingo):
        curr+=1
        if(curr%10000==0): print(curr)
        bingo = test45(curr)

def euler50():
    primesList(1000000,currPrimes)
    maxLen = 547
    for i in range(547,1,-1):
        if(hasPrimeAtLength(i)):
            print('Bingo at length: '+str(i))
            break

def hasPrimeAtLength(length):
    if(length%2==0):
        #if the length is even, we must start with two
        currSeq = [currPrimes[i] for i in range(0,length)]
        testSum=0
        for i in currSeq:
            testSum+=i
        if(testSum<1000000 and isPrime(testSum,currPrimes)):
            print('Bingo: '+str(testSum))
            return True
        return False
    tempPrimes = [i for i in currPrimes]
    tempPrimes.remove(2)
    baseSum = 0
    for i in range(0,length):
        baseSum+=tempPrimes[i]
        if(baseSum>1000000): return False
    if(isPrime(baseSum,currPrimes)):
        print('Bingo: '+str(baseSum))
        return True
    nextInd = length-1
    removeInd = -1
    while(nextInd<len(tempPrimes)):
        nextInd+=1
        removeInd+=1
        baseSum-=tempPrimes[removeInd]
        baseSum+=tempPrimes[nextInd]
        if(baseSum>=1000000): return False
        if(isPrime(baseSum,currPrimes)):
            print('Bingo: '+str(baseSum))
            return True
    return False

def continuedFractionFactory(nums):
    currentTopLevel = -1
    for i in range(len(nums)-1,-1,-1):
        if(currentTopLevel==-1):
            currentTopLevel = continuedFraction(nums[i],0)
        else:
            currentTopLevel = continuedFraction(nums[i],currentTopLevel)
    return currentTopLevel

class rational():

    def __init__(self,num,div):
        self.Numerator = num
        self.Divisor = div

    def reduce(self):
        theGCD = gcd(self.Numerator,self.Divisor)
        self.Numerator = self.Numerator//theGCD
        self.Divisor = self.Divisor//theGCD

    def __str__(self):
        return str(self.Numerator)+"/"+str(self.Divisor)
    
class continuedFraction():
    def __init__(self,a,b):
        self.A = a
        self.B = b

    def isMin(self):
        return (type(self.B)==type(1))

    def getNthConvergent(self,n):
        if(n==0): return 0
        if(n==1): return rational(self.A,1)
        if(n==2):
            if(self.isMin()):
                r = rational(self.A*self.B+1,self.B)
                #print(r)
                return r
            else:
                r = rational(self.A*self.B.A+1,self.B.A)
                #print(r)
                return r
        x = self.B.getNthConvergent(n-1)
        tempNum = x.Divisor + x.Numerator*self.A
        tempDiv = x.Numerator
        r = rational(tempNum,tempDiv)
       # print(r)
        return r

    def __str__(self):
        return str(self.A) + "," + str(self.B)

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def eContinuedN(n):
    if(n==0): return 2
    modN = n%3
    if(modN!=2): return 1
    return 2*(1+((n-modN)//3))

def euler65():
    eList = [eContinuedN(i) for i in range(0,103)]
    eContinuedFraction = continuedFractionFactory(eList)
    eHunConvergent = eContinuedFraction.getNthConvergent(100)
    print(eHunConvergent)
    eHunConvergent.reduce()
    print(eHunConvergent)
