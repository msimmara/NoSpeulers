import math

class ContinuedFractionIrrationalSquare:
    def __init__(self,N):
        self.N = int(N)
        self.NodeList = []
        self.PeriodCalculated = False
        self.PeriodLength = 0
        self.MaxIterations = 10000 #Just a sanity check so we don't loop forever, could name this better but no one will ever see it

    def GenerateFirstNode(self):
        FirstA = math.floor(math.sqrt(self.N))
        FirstB = -FirstA
        FirstD = 1
        return ContinuedFractionIrrationalSquareNode(self.N,FirstA,FirstB,FirstD)
        
    def getPeriodLength(self):
        if(self.PeriodCalculated==False):
            self.calculatePeriod()
        return self.PeriodLength

    def getPQ(self):#This is just the rational approximation of the period + 1
        if(self.PeriodCalculated==False):
            self.calculatePeriod()
        return self.getRationalApproximation(self.PeriodLength)

    def getA(self,n):
        if(self.PeriodCalculated==False):
            self.calculatePeriod()
        moddedIndex = ((n-1)%self.PeriodLength)+1
        if(n==0):
            moddedIndex=0
        return self.NodeList[moddedIndex].getA()

    def getRationalApproximation(self,n):
        currentX = 1
        currentY = self.getA(n)
        for i in range(1,n+1):
            nextX = currentY
            nextY = currentY*self.getA(n-i)+currentX
            currentX = nextX
            currentY = nextY
        return currentY,currentX,(currentY/currentX)

    def calculatePeriod(self):
        if(math.pow(math.floor(math.sqrt(self.N)),2)==self.N): #check if this is a square number, if so we don't care about this shit
            return 0
        periodFound = False
        currIter = 0
        self.NodeList = [self.GenerateFirstNode()]
        #print("Intial node: ")
        #self.NodeList[-1].printMe()
        while(not periodFound and currIter<self.MaxIterations): 
            currIter+=1
            NextNode = (self.NodeList[-1].getNext())
            #print("Next Node ("+str(currIter)+") is: ")
            #NextNode.printMe()
            innerIter = -1
            for node in self.NodeList: #Think you only ever need to check against the first?
                innerIter+=1
                if(NextNode.isEqual(node)):
                    periodFound = True
                    period = currIter-innerIter
                    self.PeriodLength = period
                    self.PeriodCalculated = True
                    #print(str(self.N)+" has period "+str(period))
                    #print(str(self.N)+" repeating sequence starts at "+str(innerIter)+" and ends at "+str(currIter))
                    #return period
            self.NodeList.append(NextNode)
     
            
    

class ContinuedFractionIrrationalSquareNode:

    def __init__(self,N,A,B,D):
        self.N = int(N)
        self.A = int(A)
        self.B = int(B)
        self.D = int(D)

    def isEqual(self,otherNode):
        return ((self.N==otherNode.N) and (self.A==otherNode.A) and (self.B==otherNode.B) and (self.D==otherNode.D)) 

    def getNext(self):
        NextD = self.getNextD()
        NextA = math.floor((math.sqrt(self.N)-self.B)/NextD)
        NextB = (0-self.B)-(NextD*NextA)
        return ContinuedFractionIrrationalSquareNode(self.N,NextA,NextB,NextD)

    def getNextD(self):
        CurrDenom = self.N - (self.B * self.B)
        nextD = int(CurrDenom/self.D)
        return nextD

    def getA(self):
        return self.A

    def printMe(self):
        result = "A: " +str(self.A)
        result+= ", B: " +str(self.B)
        result+= ", D: " +str(self.D)
        result+= ", N: " +str(self.N)
        print(result)

def Euler63():
    oddPeriodCount = 0
    for i in range(2,10001):
        currentCF = ContinuedFractionIrrationalSquare(i)
        currPeriod = currentCF.getPeriodLength()
        if(currPeriod%2==1):
            oddPeriodCount+=1

    print("Odd period count: "+str(oddPeriodCount))

def getNDigitsForRational(a,b,n):
    #a/b to the Nth digit
    digits = []
    currentA = a
    for i in range(0,n):
        newD = math.floor(currentA/b)
        newA = (currentA%b)*10
        digits.append(newD)
        currentA = newA
    return digits

def Euler80():
    sumOfSums = 0
    allDigs = []
    for i in range(2,100):
        isSquare = ((math.floor(math.sqrt(i)))*(math.floor(math.sqrt(i)))==i)
        if(isSquare):
            newArr = [i]
            allDigs.append(newArr)
            continue
        currentCF = ContinuedFractionIrrationalSquare(i)
        a,b,app = currentCF.getRationalApproximation(1000)
        currDigs = getNDigitsForRational(a,b,100)
        currSum = 0
        for dig in currDigs:
            currSum+=dig
        sumOfSums+=currSum
    print(sumOfSums)

def Euler66():
    highestX = -1
    highestD = -1
    for i in range(2,1000):
        isSquare = ((math.floor(math.sqrt(i)))*(math.floor(math.sqrt(i)))==i)
        if(isSquare):
            continue
        currentCF = ContinuedFractionIrrationalSquare(i)
        p,q,app = currentCF.getPQ()
        currPeriod = currentCF.getPeriodLength()
        x=-1
        y=-1
        
        if(currPeriod%2==0):
            print("Period for "+str(i)+" is even: "+str(currPeriod))
            x=p
            y=q
        else:
            print("Period for "+str(i)+" is odd: "+str(currPeriod))
            x=p*p+q*q*i
            y=2*p*q
        print(str(x)+"^2 - "+str(i)+"*"+str(y)+"^2 = 1")
        if(x>highestX):
            highestX = x
            highestD = i
    print("Highest D: "+str(highestD))
Euler66()

        
