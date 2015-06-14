import Euler
import RomanData
import Keylog79
import math

RomanNumeralMapping = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
SubtractivePairs = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

#test XXXXVIIII, XXXXIX, XLVIIII, and XLIX

def totalCharacters(inArr):
    charSum = 0
    for i in inArr:
        charSum += len(i)
    return charSum

def RomanEuler():
    initialSum = totalCharacters(RomanData.romanData)
    minimizedList = [minimizeRomanNumeral(i) for i in RomanData.romanData]
    newSum = totalCharacters(minimizedList)
    diff = initialSum - newSum
    print(initialSum)
    print(newSum)
    print(diff)

def minimizeRomanNumeral(romNum):
    integerForm = parseRomanNumeral(romNum)
    return minimumRoman(integerForm)

def parseRomanNumeral(romNum):
    done = False
    tempSum = 0
    tempNum = [d for d in romNum]
    while(len(tempNum)):
        if(len(tempNum)>=2):
            tempPair = SubtractivePairs.get(str(tempNum[0])+str(tempNum[1]))
            if(tempPair):
                tempSum+=tempPair
                tempNum = tempNum[2:]
                continue
        tempSum += RomanNumeralMapping[str(tempNum[0])]
        tempNum = tempNum[1:]
    return tempSum

def minimumRoman(integerForm):
    currentLeft = integerForm
    currentResult = ''
    while(currentLeft>=1000):
        currentLeft-=1000
        currentResult+='M'
    if(currentLeft>=900):
        currentResult+='CM'
        currentLeft-=900
    while(currentLeft>=500):
        currentLeft-=500
        currentResult+='D'
    if(currentLeft>=400):
        currentResult+='CD'
        currentLeft-=400
    while(currentLeft>=100):
        currentLeft-=100
        currentResult+='C'
    if(currentLeft>=90):
        currentResult+='XC'
        currentLeft-=90
    while(currentLeft>=50):
        currentLeft-=50
        currentResult+='M'
    if(currentLeft>=40):
        currentResult+='XL'
        currentLeft-=40
    while(currentLeft>=10):
        currentLeft-=10
        currentResult+='X'
    if(currentLeft>=9):
        currentResult+='IX'
        currentLeft-=9
    while(currentLeft>=5):
        currentLeft-=5
        currentResult+='V'
    if(currentLeft>=4):
        currentResult+='IV'
        currentLeft-=4
    while(currentLeft>=1):
        currentResult+='I'
        currentLeft-=1
    return currentResult

def euler79():
    possibleMins = []
    for i in Keylog.keylog:
        possibleMins = getUpdatePossibleMins(i,possibleMins)

def getUpdatePossibleMins(num,currMins):
    if(len(currMins==0)):
        currMins = [str(num)]
        return currMins
    tempMins = []
    for c in currMins:
        tempList = minCombo(c,num)
        tempMins+=tempList

def minComboThree(longer,three):
    tempList = []
    ind1 = longer.find(three[0])
    ind2 = longer.find(three[1])
    ind3 = longer.find(three[2])
    
    

def hits1Or89(num):
    curr = num
    while(curr!=89 and curr!=1):
        tempStr = str(curr)
        tempSum = 0
        for d in tempStr:
            tempSum +=(int(d)**2)
        curr = tempSum
    return curr

tempWhatevs = []

def euler92():
    global tempWhatevs
    nums = [-1 for i in range(0,568)]
    for i in range(1,568):
        nums[i] = hits1Or89(i)
    temp89Sum = 0
    for i in range(1,10000000):
        tempNum = 0
        if(i<568):
            tempNum = nums[i]
        else:
            tempNum = nums[squareSums(i)]
        if(tempNum==89): temp89Sum+=1
    print(temp89Sum)

def squareSums(n):
    result = 0;
    while (n):
        result += (n%10)*(n%10)
        n=n//10
    return result;
    

def combineStrings(a,three):
    results = []
    for i in range(0,len(a)+1):
        for k in range(i,len(a)+1):
            for j in range(k,len(a)+1):
                    temp = a[:i]+three[0]+a[i:k]+three[1]+a[k:j]+three[2]+a[j:]
                    results.append(temp)    
    return results

def euler79():
    tempKeylog = [i for i in Keylog79.keylog]
    tempKeylog.sort()
    theInput = []
    last=''
    for i in tempKeylog:
        if(i!=last):
            theInput.append(i)
            last=i
    tempCurrPossible = tempKeylog[:1]
    maximum = len(tempKeylog)
    #maximum = 6
    for i in range(1,maximum):
        tempCurrPossible = addToPossible(tempCurrPossible,tempKeylog[i],i)
    if(len(tempCurrPossible)==1): print(tempCurrPossible[0])
    else: print('Multiple possible values found')
    return tempCurrPossible

def dupePrune(a):
    tempStr = ''
    last = ''
    for i in a:
        if(i!=last):
            tempStr+=i
            last=i
    return tempStr

def addToPossible(currentList,three,deb):
    tempNewList = []
    smallestLen = 10000
    tempCombined=[]
    for i in currentList:
        tempCombined = combineStrings(i,three)
        for j in range(0,len(tempCombined)):
            tempCombined[j] = dupePrune(tempCombined[j])
            if(len(tempCombined[j])<smallestLen):
                smallestLen = len(tempCombined[j])
        tempNewList+=tempCombined
    #add smalls
    result = []
    last = ''
    for x in tempNewList:
        if(len(x)<=smallestLen and x!=last):
            result.append(x)
            last = x
    return result

def euler144():
    endPoint = Point(0.0,10.0)
    startPoint = Point(0.0,10.1)
    p2 = Point(1.4,-9.6)
    lastPoint = startPoint
    currentPoint = p2
    count = 0
    while(currentPoint!=None and not endPoint.epsilonEquals(currentPoint)):
        count+=1
        lastPoint,currentPoint = currentPoint,getNextPoint(lastPoint,currentPoint)          
    
def getNextPoint(pointA,pointB):
    pointC = None

    currentSlope = (pointB.Y-pointA.Y)/(pointB.X-pointA.X)
    currentAngle = math.atan(currentSlope)
    slopeAtB = -4*pointB.X/pointB.Y
    angleAtB = math.atan(slopeAtB)

    normAngle = angleAtB+(math.pi/2)
    newAngle = normAngle+(normAngle-currentAngle)
    
    distance = math.sqrt((pointB.X-pointA.X)**2+(pointB.Y-pointA.Y)**2)
    
    print(currentSlope)
    print(slopeAtB)
    
    print(currentAngle)
    print(angleAtB)
    
    print(normAngle)
    print(newAngle)
    
    return pointC

class Point():
    def __init__(self,x,y):
        self.X = x
        self.Y = y

    def epsilonEquals(self,point):
        epsilon = 0.001
        return(abs(self.X-point.X)<=epsilon and abs(self.Y-point.Y)<=epsilon)

def naiveResilience(num):
    if(num==1): return 0/num
    if(Euler.isPrime(num,Euler.currPrimes)): return (num-1)/num
    count = 1
    for i in range(2,num):
        hit = False
        b = math.sqrt(num)
        for p in Euler.currPrimes:
            if(p>b): break
            if(i%p==0 and num%p==0):
                hit = True
                break
        if(not hit): count+=1
    return count/num

def euler243():
    target = 15499/94744
    currentD = 1
    nextFactor = 2
    currFactorIndex = 0
    currR = 1
    while(currR>=target):
        print('Current index '+str(currFactorIndex))
        print('Current D '+str(currentD))
        currFactorIndex+=1
        if(len(Euler.currPrimes)<=currFactorIndex):
            Euler.currPrimes = Euler.primesList(nextFactor*2,Euler.currPrimes)
        nextFactor = Euler.currPrimes[currFactorIndex]
        currentD*=nextFactor
        currR = naiveResilience(currentD)
    print('D'+str(currentD))
    print('R'+str(currR))

def euler243Heuristic():
    target = 15499/94744
    currentD = 1
    nextFactor = 2
    currFactorIndex = 0
    currR = 1
    while(currR>=target or True):
        currFactorIndex+=1
        if(len(Euler.currPrimes)<=currFactorIndex):
            Euler.currPrimes = Euler.primesList(nextFactor*2,Euler.currPrimes)
        nextFactor = Euler.currPrimes[currFactorIndex]
        currentD*=nextFactor
        currR = pseudoResilience(currFactorIndex)
        if(currR<target):
            print('Pseudo hit on Index '+str(currFactorIndex))
            print(currentD)
            print(currR)
        
    print('D'+str(currentD))
    print('R'+str(currR))

def pseudoResilience(primeN):
    currentR = 1
    for i in range(0,primeN+1):
        currentR*=((Euler.currPrimes[i])-1)/(Euler.currPrimes[i])
    return currentR

CurrentWildcardLists = [[]]
PossibleChars = ['1','2','3','4','5','6','7','8','9','0','*']

Euler.primesList(100000,Euler.currPrimes)
print('sdf')

def starifiedList(stars,num):
    if(stars==1):
        starOne = []
        for i in range(0,len(str(num))):
            starOne.append(str(num)[0:i]+"*"+str(num)[i+1:])
        return starOne
    lastStarified = starifiedList(stars-1,num)
    for currLast = #todo loop through and whatever
    
        


