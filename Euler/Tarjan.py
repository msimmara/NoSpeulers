class Vertex:
    
    def __init__(self,value):
        self.index = -1
        self.lowLink = -1
        self.onStack = False
        self.edges = []
        self.value = value
        self.MarkForRemoval = False
        
    def addEdge(self,vert):
        self.Edges.append(vert)


def tarjan(V):  
    index = [0]
    S = []
    SCCs = []
    for v in V:
        if (v.index ==-1):
            strongconnect(v,index,S,SCCs)
    return SCCs
    
currentSCC = []

def strongconnect(v,indPoint,S,SCCs):
    global currentSCC
    #Set the depth index for v to the smallest unused index
    v.index = indPoint[0]
    v.lowlink = indPoint[0]
    indPoint[0]+=1
    S.append(v)
    v.onStack = True
    #Consider successors of v
    for w in v.edges:
        if (w.index==-1):
            # Successor w has not yet been visited; recurse on it
            strongconnect(w,indPoint,S,SCCs)
            v.lowlink  = v.lowlink if (v.lowLink<w.lowLink) else w.lowlink
        elif (w.onStack):
            # Successor w is in stack S and hence in the current SCC
            v.lowlink  = v.lowlink if v.lowLink<w.index else w.index
            currentSCC.append(w)
      

    # If v is a root node, pop the stack and generate an SCC
    
    if(v.lowlink == v.index):    
        #start a new strongly connected component
        #repeat
        newSCC = []
        while(True):
            w = S.pop()
            w.onStack = False
            newSCC.append(w)
            if(w==v):
                break
        SCCs.append(newSCC)
        #add w to current strongly connected component
        #until (w = v)
        #output the current strongly connected component