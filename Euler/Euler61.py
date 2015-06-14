import EulerLib

def getFourDigPolys():
    fourDigPolys = []
    for i in range(3,9):
        fourDigPolys.append([])
        currNum = 0
        ct = 1
        while(currNum<10000):
            currNum=EulerLib.getPolygonalNumber(i, ct)
            ct+=1
            if(currNum>1000 and currNum<10000):
                fourDigPolys[-1].append(currNum)
    return fourDigPolys

def euler61C():
    fourDigPolys = getFourDigPolys()
    printLens(fourDigPolys)
    
    for i in range(0,20):
            for n in range(0,6):
                reducePoly(n, fourDigPolys)
    printLens(fourDigPolys)
    
    currCands = []
    
    for t in fourDigPolys[0]:
        currCands.append(CycleCandidate(t,-1,-1,-1,-1,-1,[0]))
      
    currCands = updateCands(currCands, fourDigPolys)  
    currCands = updateCands(currCands, fourDigPolys)  
    currCands = updateCands(currCands, fourDigPolys)
    currCands = updateCands(currCands, fourDigPolys)
    currCands = updateCands(currCands, fourDigPolys)
    
          
    
    
    #for t in fourDigPolys[0]:    
    
def updateCands(currendCandidates,fourDigitPolys):
    nextCands = []
        
    for cand in currendCandidates:
        currNexts = cand.getNextCandidates(fourDigitPolys)
        nextCands.extend(currNexts)
        
    return nextCands
    
def printLens(fourDigPolys):
    prod = 1
    n = -1
    for p in fourDigPolys:
        prod*=len(p)
        n+=1
        print("Len "+str(n)+": "+str(len(p)))
        
def reducePoly(n,fourDigPolys):
    newN = []
    for p in fourDigPolys[n]:
        currN = -1
        matchFound1 = False
        matchFound2 = False
        for pList in fourDigPolys:
            currN+=1
            if(currN==n):
                continue
            for pCurr in pList:
                if(isOrderedCycleCand(p, pCurr)):
                    matchFound1 = True
                if(isOrderedCycleCand(pCurr, p)):
                    matchFound2 = True
                if(matchFound1 and matchFound2):
                    break
                
            if(matchFound1 and matchFound2):
                break
        if(matchFound1 and matchFound2):
            newN.append(p)
    fourDigPolys[n] = newN
            

def euler61B():
    fourDigPolys = getFourDigPolys()
    
    prod = 1
    for p in fourDigPolys:
        prod*=len(p)
        print("Len p: "+str(len(p)))
      
    sharesWithAnyT = []  
    tSharesWithAny = []
    for t in fourDigPolys[0]:
        n=1
        mFound = False
        ct = 0
        print(t)
        for ps in fourDigPolys[1:]:
            print("\t"+str(n))
            for p in ps:
                if(isOrderedCycleCand(t, p)):
                    sharesWithAnyT.append(CycCandidate(n,p,t))
                    print("\t\t"+str(p))
                    mFound = True
            n+=1
        if(mFound):
            tSharesWithAny.append(t)
            
    sharesWithCand = []        
    for cand in sharesWithAnyT:
        currPolyPoss = fourDigPolys[1:cand.N] + fourDigPolys[cand.N+1:]
        for ps in currPolyPoss:
            for p in ps:
                if(sharesSomething(cand.Poly, p) or sharesSomething(cand.T, p)):
                    sharesWithCand.append(p)
    
              
                    
    print(len(sharesWithAnyT))
    print(len(sharesWithCand))
    print(len(tSharesWithAny))
    
def euler61():
    fourDigPolys = []
    for i in range(3,9):
        fourDigPolys.append([])
        currNum = 0
        ct = 1
        while(currNum<10000):
            currNum=EulerLib.getPolygonalNumber(i, ct)
            ct+=1
            if(currNum>1000 and currNum<10000):
                fourDigPolys[-1].append(currNum)

class CycleCandidate:
    
    def __init__(self,p3,p4,p5,p6,p7,p8,order):
        self.P = []
        self.P.append(p3)
        self.P.append(p4)
        self.P.append(p5)
        self.P.append(p6)
        self.P.append(p7)
        self.P.append(p8)
        self.HasValue = [p3>0,p4>0,p5>0,p6>0,p7>0,p8>0]   
        self.Order = order
    
    def setPolyByN(self,n,poly):
        self.P[n-3] = poly
    
    def printCandidate(self):
        print(self.Order)
        print(self.P)
        
    def getNextCandidates(self,fourDigitPolys):
        ct = -1
        totalLoops = 0
        results = []
        last = self.P[self.Order[-1]]
        for fdpl in fourDigitPolys:
            ct+=1                
            for curr in fdpl:
                totalLoops+=1
                if(isOrderedCycleCand(curr,last) and self.P[ct]<=0):
                    newOrder = [i for i in self.Order]
                    newOrder.append(ct)
                    tempP = [p for p in self.P]
                    tempP[ct] = curr
                    newRes = CycleCandidate(tempP[0],tempP[1],tempP[2],tempP[3],tempP[4],tempP[5],newOrder)
                    results.append(newRes)
                    if(len(newOrder)==6 and isOrderedCycleCand(newRes.P[newRes.Order[0]],curr)):
                        newRes.printCandidate()
        #print(totalLoops)
        return results
                    
            
            
    
class CycCandidate:
    def __init__(self,n,poly,t):
        self.N = n
        self.Poly= poly
        self.T = t

def sharesSomething(a,b):
    strA = str(a)
    strB = str(b)
    return strA[:2]==strB[2:] or strB[:2]==strA[2:]

def isOrderedCycleCand(a,b):
    strA = str(a)
    strB = str(b)
    return strA[:2]==strB[2:]# or strB[:2]==strA[2:]
          
euler61C()