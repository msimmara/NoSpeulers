import EulerLib
import PrimeHelper
import math
from operator import itemgetter

ph = PrimeHelper.PrimeHelper()

def euler58():
    spiral = Spiral()
    spiral.addLevel()
    diagonalCount = 4
    primeCount = 3
    primePercent = primeCount/diagonalCount
    while(primePercent>.1):
        spiral.addLevel()
        diagonalCount+=4
        currCorners = spiral.getCorners()
        for c in currCorners:
            if(ph.isPrime(c)):
                primeCount+=1
        primePercent = primeCount/diagonalCount
    print(spiral.SideLength)
        
    
    
class Spiral:
    def __init__(self):
        self.SideLength = 1
        self.HighNumber = 1
    
    def addLevel(self):
        self.SideLength+=2
        delta = (self.SideLength*4)-4
        self.HighNumber+=delta
    
    def getCorners(self):
        return [self.HighNumber,self.HighNumber-((self.SideLength-1)*1),self.HighNumber-((self.SideLength-1)*2),self.HighNumber-((self.SideLength-1)*3)]
    
    def getCorner(self,RorL,UorD):
        if(self.SideLength==1):
            return 1
        if(RorL=="R"):
            if(UorD=="D"):
                return self.HighNumber
            return self.HighNumber-((self.SideLength-1)*3)
        if(UorD=="D"):
            return self.HighNumber-((self.SideLength-1))
        return self.HighNumber-((self.SideLength-1)*2)
       
        


    
euler58()