#must move exactly 79 times to the right, 79 times down


matFileName = "C:\\Users\\michael.simmarano\\Desktop\\matrix81.txt"
matFile = open(matFileName)

matrix81 = []
for i in range(0,80):
    currentLine = matFile.readline()    
    currentNums = currentLine.split(',')
    matrix81.append([])
    currMatLine = matrix81[-1]
    for i in range(0,80):
        currMatLine.append(int(currentNums[i]))

samepleMatrix = [[131,673,234,103,18],
                 [201,96,342,965,150],
                 [630,803,746,422,111],
                 [537,699,497,121,956],
                 [805,732,524,37,331]]

    


theMatrix = matrix81
l = 80

#theMatrix = samepleMatrix
#l = 5

baseSum = theMatrix[0][0]
cursorRow = 0
cursorCol = 0
thePath = []

while(cursorRow!=l-1 or cursorCol!=l-1):
    if(cursorRow==l-1):
        cursorCol+=1
        thePath.append('R')
    elif (cursorCol==l-1):
        cursorRow+=1
        thePath.append('D')
    else:
        downDelta = theMatrix[cursorRow+1][cursorCol]
        rightDelta = theMatrix[cursorRow][cursorCol+1]
        if(downDelta<=rightDelta):
            cursorRow+=1
            thePath.append('D')
        else:
            cursorCol+=1
            thePath.append('R')
    baseSum+=theMatrix[cursorRow][cursorCol]

def naivePath(startRow,startCol,endRow,endCol,matrix):
    baseSum = matrix[0][0]
    cursorRow = 0
    cursorCol = 0
    thePath = []
    while(cursorRow!=l-1 or cursorCol!=l-1):
        if(cursorRow==l-1):
            cursorCol+=1
            thePath.append('R')
        elif (cursorCol==l-1):
            cursorRow+=1
            thePath.append('D')
        else:
            downDelta = matrix[cursorRow+1][cursorCol]
            rightDelta = matrix[cursorRow][cursorCol+1]
            if(downDelta<=rightDelta):
                cursorRow+=1
                thePath.append('D')
            else:
                cursorCol+=1
                thePath.append('R')
        baseSum+=matrix[cursorRow][cursorCol]
    return basesum,thePath
    
knownMinPathSums = []
knownMinPaths = []

def initMinTables(length):
    for i in range(0,l):
        knownMinPathSums.append([])
        knownMinPaths.append([])
        currSumLine = knownMinPathSums[-1]
        currPathLine = knownMinPaths[-1]
        for j in range(0,l):
            currSumLine.append(-1)
            currPathLine.append('')
        

def setMinPath(startRow,startCol,minSum,minPath):
    knownMinPathSums[startRow][startCol] = minSum
    knownMinPaths[startRow][startCol] = minPath
    
def hasMinPath(startRow,startCol):
    return knownMinPathSums[startRow][startCol]!=-1

def test81():
	initMinTables(80)
	s,p = minPathFrom(0,0,79,79,matrix81)

def minPathFrom(startRow,startCol,endRow,endCol,matrix):
    if hasMinPath(startRow,startCol):
        return knownMinPathSums[startRow][startCol], knownMinPathSums[startRow][startCol]
    currPath = []
    currSum = matrix[startRow][startCol]
    if(endRow==startRow):
        currCol = startCol
        while(currCol!=endCol):
            currCol+=1
            currPath.append('R')
            currSum+=matrix[startRow][currCol]
            
        setMinPath(startRow,startCol,currSum,currPath)
        return currSum,currPath
    if(endCol==startCol):
        currRow = startRow
        currSum = matrix[startRow][startCol]
        while(currRow!=endRow):
            currRow+=1
            currPath.append('D')
            currSum+=matrix[currRow][startCol]
            
        setMinPath(startRow,startCol,currSum,currPath)
        return currSum,currPath
    
    s1,p1 = minPathFrom(startRow,startCol+1,endRow,endCol,matrix) #R
    s2,p2 = minPathFrom(startRow+1,startCol,endRow,endCol,matrix) #D

    if(s1<s2):
        currSum+=s1
        currPath.append('R')
    else:
        currSum+=s2
        currPath.append('D')
    setMinPath(startRow,startCol,currSum,currPath)
    return currSum,currPath
        
