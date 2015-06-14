import EulerLib
import PrimeHelper
import Tarjan

ph = PrimeHelper.PrimeHelper()

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
    for i in range(1,n+1):
        currP = ph.getNthPrime(i)
        #print(currP)
        currN = Tarjan.Vertex(currP)
        nodes.append(currN)
    edgeCount = 0
    for node in nodes:
        for compNode in nodes:
            if((not compNode==node) and (checkConcatProp(node.value, compNode.value)) ):
                node.edges.append(compNode)
                edgeCount+=1

    return nodes,edgeCount

def sumCand(cand):
    theSum = 0
    for i in cand:
        theSum+=i
    return theSum

def euler60C():
    cands = []
    highestNs = []
    n=800
    ph.updatePrimesToN(8000)
    print("Primes primed")
    #set initial candidate
    for i in range(2,500):
        primeI = ph.getNthPrime(i)
        for j in range(i+1,1000):
            primeJ = ph.getNthPrime(j)
            if(checkConcatProp(primeI,primeJ)):
                newCand = [primeI,primeJ]
                highestNs.append(j)
                cands.append(newCand)
    
    print(len(cands))
    
    cands,highestNs = updateCands(cands,highestNs,2000)
    print(len(cands))    
    cands,highestNs = updateCands(cands,highestNs,5000)
    print(len(cands))
    cands,highestNs = updateCands(cands,highestNs,80000)
    print(len(cands))
    
    #for c in cands:
     #   print(c + " summed = "+str(sumCand(c)))
    
    
def updateCands(cands,highNs,n):
    newCands = []
    newHighNs = []
    ct=-1
    for c in cands:
        ct+=1
        for i in range(highNs[ct],n):
            primeI = ph.getNthPrime(i)
            if(checkConcatCand(c, primeI)):
                newCand = []
                theS = 0
                for p in c:
                    newCand.append(p)
                    theS+=p
                newCand.append(primeI)
                theS+=primeI
                if(len(newCand)>=5):
                    print(newCand)
                    print(theS)
                newCands.append(newCand)
                newHighNs.append(i)
                
    return newCands,newHighNs

def euler60b():
    graph,edgeCount = buildGraphUnderN(800)
    #print(edgeIntersection(graph[3], 4))
    print("Graph built: "+str(len(graph))+" nodes and "+str(edgeCount)+ " edges.")
    graph,edgeCount = reduceUntilStable(graph,edgeCount,5)
    print("Graph reduced: "+str(len(graph))+" nodes and "+str(edgeCount)+ " edges.")
    
    #Here be crazy shit
    cursors = [0,1,2,3,4]
    updates = 0
    cands = []
    gLen = len(graph)
    maxes = [5,10,int(gLen/3),int(gLen/2),gLen-1]
    while(updateCursors(cursors, maxes)):
        updates+=1
        #print("Update: "+str(updates))
        #print(cursors[-1])
        currList = [graph[i].value for i in cursors]
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
    
   
    
    
    
     
def reduceUntilStable(graph,currEdgeCount, n):
    while(True):
        newG,newEdge = reduceGraph(graph, n)
        if(newEdge==currEdgeCount and len(newG)==len(graph)):
            return newG,newEdge
        graph = newG
        currEdgeCount = newEdge
     
def reduceGraph(graph, n):
    gLen = len(graph)
    for i in range(0,gLen):
        v = graph[i]
        if (len(v.edges)<n-1):
            v.MarkForRemoval = True
    
    graph, edgeCount = removeMarked(graph)
    
    gLen = len(graph)
    for i in range(0,gLen):
        v = graph[i]
        if (edgeIntersection(v,n-1)<n-1):
            v.MarkForRemoval = True
    
    
    graph, edgeCount = removeMarked(graph)
            
    return removeMarked(graph)

def edgeIntersection(v,n):
    totalInter = 0
    for e in v.edges:
        currC = 0
        for subE in e.edges:
            if(subE in v.edges):
                currC+=1
                
        if(currC>=n-1):
            totalInter+=1
            
    return totalInter

def removeMarked(graph):
    newGraph = []
    edgeCount=0
    gLen = len(graph)
    for i in range(0,gLen):
        v = graph[i]
        if(not v.MarkForRemoval):
            newEdges = []
            for e in v.edges:
                if(not e.MarkForRemoval):
                    newEdges.append(e)
                    edgeCount+=1
            v.edges = newEdges
            newGraph.append(v)
            
    return newGraph,edgeCount

def printSCC(scc):
    strP = "["
    for v in scc:
        strP+=str(v.value)+" "
    strP+="]"
    print(strP)
    
def updateCursors(cursors,maxes):
    cLen = len(cursors)
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
        
    for i in range(cLen-1,-1,-1):
        if(cursors[i]>maxes[i]):
            print("Maxed on")
            print(maxedOn)
            return False
    
    return True

euler60C()


