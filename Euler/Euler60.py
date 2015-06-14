import EulerLib
import PrimeHelper

ph = PrimeHelper.PrimeHelper()

class PNode:
    
    def __init__(self,p):
        self.P = p
        self.Links = []
        self.Visited = False
        
    def addLink(self,linkedNode):
        self.Links.append(linkedNode)
        
    def setVisited(self,t):
        self.Visited = t

def euler60():
    currList = [3,7,109,673]
    currP = 2
    n = 0
    while(currP<673):
        n+=1
        currP = ph.getNthPrime(n)
        
    found = False
    while(not found):
        n+=1
        currP = ph.getNthPrime(n)         
        found = checkConcatCand(currList, currP)
        print(currP)
    if(found):
        print(currP)
    
def checkConcatCand(initList,cand):
    for il in initList:
        currRes = checkConcatProp(il,cand)
        if(not currRes):
            return False
    return True

def checkConcatProp(il,cand):
    front = str(il)+str(cand)
    back = str(cand)+str(il)
    return(ph.isPrime(int(front)) and ph.isPrime(int(back)))

def buildGraphUnderN(n):
    nodes = []
    for i in range(1,n):
        currP = ph.getNthPrime(i)
        #print(currP)
        currN = PNode(currP)
        nodes.append(currN)
    for node in nodes:
        for compNode in nodes:
            if((not compNode==node) and (checkConcatProp(node.P, compNode.P)) ):
                node.Links.append(compNode)
        #if(len(node.Links)>3):
         #   print("Lots o' links! "+str(node.P))
          #  print("Link count "+str(len(node.Links)))
    print(len(nodes))
    return nodes

def findConnectedSubGraph(nodes,n):
    for node in nodes:
        node.Visited = True
        if (len(node.Links)>=(n-1)):
            subG = []
            subG.append(node)
            for l in node.Links:
                if(len(l.Links)>=(n-1)):    
                    subG.append(l)
            
            subGLen = len(subG)
            while(True and subGLen>0):
                subG = reduceSG(subG,n)
                if(len(subG)==subGLen or len(subG)<n):
                    break
                subGLen = len(subG)
            
            if(len(subG)>=n):
                sgPr = ""
                for sg in subG:
                    sgPr += str(sg.P)+" ["
                    for sgl in sg.Links:
                        if(sgl in subG):
                            sgPr+= str(sgl.P)+ " "
                    sgPr+="] "
                print(sgPr+"|")
            
def reduceSG(subG,n):
    newSubG = []
    for sg in subG:
        currCt=0
        for l in sg.Links:
            if(l in subG):
                currCt+=1
        if(currCt>=(n-1)):
            newSubG.append(sg)
    return newSubG

def updateCursors(cursors,maxes,n):
    cLen = len(cursors)
    done = False
    maxedOn = -1
    for i in range(cLen-1,-1,-1):
        if(cursors[i]<maxes[i]):
            cursors[i]+=1
            maxedOn = i            
            break
    if(maxedOn==-1):
        return False
    upC = cursors[maxedOn]
    for j in range(maxedOn+1,cLen):
          upC+=1
          cursors[j] = upC
    
    return True 
        
        
    

#euler60()
#print(checkConcatCand([3,7,109], 673))
#nodes = buildGraphUnderN(1000)
#print("Looking for connected subgraph")
#findConnectedSubGraph(nodes, 5)
cursors = [1,2,3,4]
cursorN = 1000
ph.updatePrimesToN(1001)
print("Primes primed")
updates = 0
cands = []
maxes = [20,50,100,600]
while(updateCursors(cursors, maxes,cursorN)):
    updates+=1
    #print("Update: "+str(updates))
    currList = [ph.getNthPrime(i) for i in cursors]
    mismatch = False
    for cand in currList:
        for cand2 in currList:
            if(cand!=cand2 and (not checkConcatProp(cand, cand2))):
                mismatch = True
                break
    if(not mismatch):
        print("Yeah!")
        print(currList)
        cands.append(currList)

print("Looking for that 5th...")

for c in cands:
    for i in range(1,cursorN):
        currP = ph.getNthPrime(i)
        if(currP not in c and checkConcatCand(c, currP)):
            print("More yeah!")
            print(c)
            print(currP)
            
