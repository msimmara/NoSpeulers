import EulerLib
import math

class Card:
    
    def __init__(self,val,suit):
        self.Value = val
        self.Suit = suit

    def getIntVal(self):
        if(self.Value=='T'):
            return 10
        if(self.Value=='J'):
            return 11
        if(self.Value=='Q'):
            return 12
        if(self.Value=='K'):
            return 13
        if(self.Value=='A'):
            return 14
        return int(self.Value)

    def __str__(self):
        return self.Value + self.Suit
    
def printHand(hand):
    currStr = ""
    for c in hand:
        currStr+=c.__str__()+" "
    print(currStr)

def debugHands(p1Hands,p2Hands,results,i):
    print("Player 1 hand")
    printHand(p1Hands[i])
    print("Player 2 hand")
    printHand(p2Hands[i])
    print("Winner")
    print(results[i])

def readInHands():
    pokerHands = open("C:\\Users\\michael.simmarano\\Desktop\\Euler\\poker.txt")
    p1Hands = []
    p2Hands = []
    for i in range(0,1000):
        currLine = pokerHands.readline()
        currCardStrings = currLine.split(" ")
        currentHand1 = []
        currentHand2 = []
        for j in range(0,5):
            cc  = Card(currCardStrings[j][0],currCardStrings[j][1])
            currentHand1.append(cc)
        p1Hands.append(currentHand1)
        for j in range(5,10):
            cc  = Card(currCardStrings[j][0],currCardStrings[j][1])
            currentHand2.append(cc)
        p2Hands.append(currentHand2)
        return p1Hands, p2Hands
        
def euler54():
    p1Hands, p2Hands = readInHands()

    p1Wins = 0
    results = []
    for i in range(0,1000):
        currWinner = compareHands2(p1Hands[i],p2Hands[i])
        if(currWinner!=1 and currWinner!=2):
            print("Current Hand: "+str(i+1)+" Current winner: "+str(currWinner))
        results.append(currWinner)
        if(currWinner==1):
            p1Wins+=1
    print("Player one wins: "+str(p1Wins))
    return p1Hands,p2Hands,results        

def compareHands(hand1,hand2):
    hcWinner = getHighCardWinner(hand1,hand2)
    score1 = scoreHand(hand1)
    score2 = scoreHand(hand2)
    if(score1>score2):
        return 1
    if(score1<score2):
        return 2
    if(score1>=9):
        return 0
    if(score1==5 or score1==6 or score1==1):
        return hcWinner
    if(score1==2):
        vals1 = [c.getIntVal() for c in hand1]
        vals1.sort()
        vals2 = [c.getIntVal() for c in hand2]
        vals2.sort()
        pair1 = 0
        pair2 = 0
        for i in range(1,5):
            if (vals1[i]==vals1[i-1]):
                pair1 = vals1[i]
            if (vals2[i]==vals2[i-1]):
                pair2 = vals2[i]
        if(pair1>pair2):
            return 1
        if (pair2>pair1):
            return 2
        return hcWinner
    #if(score1==):

def compareHands2(hand1,hand2):
    scores1 = scoreHand3(hand1)
    scores2 = scoreHand3(hand2)
    ind = 0
    for s in scores1:
        if(s>scores2[ind]):
            return 1
        if(s<scores2[ind]):
            return 2
        ind+=1         
        

def getHighCardWinner(hand1,hand2):
    vals1 = [c.getIntVal() for c in hand1]
    vals1.sort()
    vals2 = [c.getIntVal() for c in hand2]
    vals2.sort()
    for i in range(4,-1,-1):
        if(vals1[i]==vals2[i]):
            continue
        return 1 if vals1[i]>vals2[i] else 2
    return 0

def scoreHand(hand):
    flush = isFlush(hand)
    royal = isRoyal(hand)
    if(flush and royal):
        return 10#,14,-1
    straight, highcard = isStraight(hand)
    if(straight and flush):
        return 9#, highcard,-1
    groups = checkGroups(hand)
    if(len(groups)==2):#either four of a kind or full house
        firstCard,firstCount = groups[0]
        if(firstCount==1):
            return 8#,groups[1][0],groups[0][0]
        if(firstCount==4):
            return 8#,groups[0][0],groups[1][0]
        if(firstCount==3):
            return 7#,groups[0][0],groups[1][0]
        else:
            return 7#,groups[1][0],groups[0][0]
    if(flush):
        return 6#, highcard,-1
    if(straight):
        return 5#, highcard,-1
    if(len(groups)==3):#either three of a kind or two pair
        firstCard,firstCount = groups[0]
        if(firstCount==2 or groups[1][1]==2):
            return 3
        return 4
    if(len(groups)==4):
        return 2
    return 1

def scoreHand2(hand):
    flush = isFlush(hand)
    royal = isRoyal(hand)
    if(flush and royal):
        return [10,14]
    straight, highcard = isStraight(hand)
    if(straight and flush):
        return [9, highcard]
    groups = checkGroups(hand)
    if(len(groups)==2):#either four of a kind or full house
        firstCard,firstCount = groups[0]
        if(firstCount==1):
            return [8,groups[1][0],groups[0][0]]
        if(firstCount==4):
            return [8,groups[0][0],groups[1][0]]
        if(firstCount==3):#full house
            return [7,groups[0][0],groups[1][0]]
        else:
            return [7,groups[1][0],groups[0][0]]
    if(flush):
        return [6, highcard]
    if(straight):
        return [5, highcard]
    if(len(groups)==3):#either three of a kind or two pair
        firstCard,firstCount = groups[0]
        if(firstCount==2 or groups[1][1]==2):
            pairs = []
            lastVal = 0
            for i in range(0,3):
                if(groups[i][1]==2):
                    pairs.append(groups[i][0])
                if(groups[i][1]==1):
                    lastVal = groups[i][0]
            if(pairs[0]>pairs[1]):
                return [3,pairs[0],pairs[1],lastVal]
            return [3,pairs[1],pairs[0],lastVal]
        for i in range(0,3):
            remainingCards = []
            if(groups[i][1]==3):
                three = groups[i][0]
            else:
                remainingCards.append(groups[i][0])
        return [4,groups[i][0]] + remainingCards
    if(len(groups)==4):
        pair = 0
        remainingCards = []
        for i in range(0,3):
                if(groups[i][1]==2):
                    pair =groups[i][0]
                else:
                    remainingCards.append(groups[i][0])
        remainingCards.sort()        
        return [2,pair]+remainingCards
    return [1,highcard]

def scoreHand3(hand):
    flush = isFlush(hand)
    royal = isRoyal(hand)
    if(flush and royal):
        return [10,14]
    straight, highcard = isStraight(hand)
    if(straight and flush):
        return [9, highcard]
    groups,threes,pairs = checkGroups(hand)
    if(len(groups)==2):#either four of a kind or full house
        firstCard,firstCount = groups[0]
        if(firstCount==1):
            return [8,groups[1][0],groups[0][0]]
        if(firstCount==4):
            return [8,groups[0][0],groups[1][0]]
        if(firstCount==3):#full house
            return [7,groups[0][0],groups[1][0]]
        else:
            return [7,groups[1][0],groups[0][0]]
    if(flush):
        return [6, highcard]
    if(straight):
        return [5, highcard]
    groups.sort(key=groupScore)
    if(threes==1):
        return [4] + groups
    if(pairs==2):
        return [3]+groups
    if(pairs==1):
        return [2]+groups
    return [1] + groups
    

def groupScore(group):
    return group[1]*10+group[0]
    
    
def checkGroups(hand):
    valCount = [0 for i in range(0,13)]
    for c in hand:
        valCount[c.getIntVal()-2]+=1
    groups = []
    threeC = 0
    pairC = 0
    for i in range(0,13):
        currC = valCount[i]
        if(currC>0):
            groups.append((i+2,currC))
        if(currC==3):
            threeC+=1
        if(currC==2):
            pairC+=1
    return groups,threeC,pairC

def isRoyal(hand):
    hasVal = [False for c in hand]
    for c in hand:
        currVal = c.getIntVal()-10
        if(currVal<0):
            return False
        hasVal[currVal] = True
    return (False not in hasVal)

def isStraight(hand):
    checkAceAsOne = False
    #print(hand)
    vals = [c.getIntVal() for c in hand]
    for i in range(0,5):
        v=vals[i]
        if(v==14):
            vals[i]=1
    #print(vals)
    vals.sort()
    if(vals[0]==2):#special case where Ace might need to be one
        checkAceAsOne = False
    for i in range(1,5):
        if(vals[i]!=vals[i-1]+1):
            if(not checkAceAsOne):
                return False, vals[4]
            if(i==4 and vals[i]==14):
                return True, 5
    return True, vals[4]

def isStraight2(hand):
    checkAceAsOne = False
    #print(hand)
    vals = [c.getIntVal() for c in hand]
    #print(vals)
    vals.sort()
    if(vals[0]==2):#special case where Ace might need to be one
        checkAceAsOne = True
    for i in range(1,5):
        if(vals[i]!=vals[i-1]+1):
            if(not checkAceAsOne):
                return False, vals[4]
            if(i==4 and vals[i]==14):
                return True, 5
    return True, vals[4]
    
def isFlush(hand):
    isFlush = True
    lastSuit = hand[0].Suit
    for c in hand:
        if(lastSuit!=c.Suit):
            isFlush=False
            break
    return isFlush
    
euler54()    
