import math

class PrimeHelper:
    
    def __init__(self):
        self.PrimeList = [2,3]
        self.PrimeCount = 2
        self.UpperBound = 3

    def isPrime(self,n):
        sqrtN = int(math.sqrt(n))
        self.updatePrimesToBound(sqrtN)
        for p in self.PrimeList:
            if(p>sqrtN):
                return True
            if(n%p==0):
                return False
        return True

    def updatePrimesToN(self,n):
        currentCandidate = self.UpperBound
        if(currentCandidate%2==0):
            currentCandidate-=1
        while(self.PrimeCount<n):
            currentCandidate+=2
            if(self.isPrime(currentCandidate)):
                self.PrimeCount+=1
                self.PrimeList.append(currentCandidate)
            self.UpperBound = currentCandidate

    def isInPrimeList(self,n,beginning=0,end=-2):
        if(beginning is None):
            beginning=0

        if(end==-2):
            end = self.PrimeCount-1
        
        if(beginning>=end):
            return self.PrimeList[beginning]==n
        
        middle = (beginning)+int((end-beginning)/2)
        middleP = self.PrimeList[middle]
        if(middleP==n):
            return True
        if(middleP>n):
            return self.isInPrimeList(n,beginning,middle-1)
        return self.isInPrimeList(n,middle+1,end)
        

    def updatePrimesToBound(self,bound):
        currentCandidate = self.UpperBound
        if(currentCandidate%2==0):
            currentCandidate-=1
        while(self.UpperBound<bound):
            currentCandidate+=2
            if(self.isPrime(currentCandidate)):
                self.PrimeCount+=1
                self.PrimeList.append(currentCandidate)
            self.UpperBound = currentCandidate            

    def getNthPrime(self,n):
        if(n<=0):
            return -1
        
        if(self.PrimeCount<n):
            self.updatePrimesToN(n)

        return self.PrimeList[n-1]


        
    
