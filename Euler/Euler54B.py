import EulerLib
import math
from operator import itemgetter

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
        currWinner = compareHands(p1Hands[i],p2Hands[i])
        if(currWinner!=1 and currWinner!=2):
            print("Current Hand: "+str(i+1)+" Current winner: "+str(currWinner))
        results.append(currWinner)
        if(currWinner==1):
            p1Wins+=1
    print("Player one wins: "+str(p1Wins))
    return p1Hands,p2Hands,results        

def compareHands(hand1,hand2):
    scores1 = scoreHand(hand1,1)
    scores2 = scoreHand(hand2,2)
    ind = 0
    for s in scores1:
        if(s>scores2[ind]):
            return 1
        if(s<scores2[ind]):
            return 2
        ind+=1         
        
#High Card: Highest value card.
#One Pair: Two cards of the same value.
#Two Pairs: Two different pairs.
#Three of a Kind: Three cards of the same value.
#Straight: All cards are consecutive values.
#Flush: All cards of the same suit.
#Full House: Three of a kind and a pair.
#Four of a Kind: Four cards of the same value.
#Straight Flush: All cards are consecutive values of same suit.
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.        
        
def scoreHand(hand,t):
    isFlush = checkFlush(hand)
    isStraight, sHigh = checkStraight(hand)
    isRoyal = checkRoyal(hand)
    if(isRoyal and isStraight and isFlush):
        return [10]
    if(isStraight and isFlush):
        return [9, sHigh]
    if(isFlush):
        intVals = [c.getIntVal() for c in hand]
        intVals.sort(key=None, reverse=True)
        return [6] + intVals
    if(isStraight):
        return [5, sHigh]
    grouped = getGroups(hand)
    if(grouped[0][1] == 4):  # four of a kind
        return [8, grouped[0][0], grouped[1][0]]
    if(grouped[0][1] == 3):
        if(grouped[1][1] == 2):  # full house
            return [7, grouped[0][0], grouped[1][0]]
        return [4, grouped[0][0], grouped[1][0], grouped[2][0]]  # three of a kind
    if(grouped[0][1] == 2):
        if(grouped[1][1] == 2):  # two pair
            return [3, grouped[0][0], grouped[1][0], grouped[2][0]]
        return [2, grouped[0][0], grouped[1][0], grouped[2][0], grouped[3][0]]
    return [1, grouped[0][0], grouped[1][0], grouped[2][0], grouped[3][0], grouped[4][0]]
  
def getGroups(hand):
    groups = [[] for i in range(0,15)]
    for c in hand:
        i = c.getIntVal()
        groups[i].append(i)
    results = []
    for g in groups:
        if(len(g)>0):
            results.append([g[0],len(g)])
    results.sort(key=itemgetter(0), reverse=True)
    results.sort(key=itemgetter(1), reverse=True)
    return results

def checkFlush(hand):
    lastVal = -1
    for c in hand:
        currVal = c.Suit
        if(lastVal!=-1 and currVal!=lastVal):
            return False
        lastVal = currVal
    return True

def checkStraight(hand):
    intVals = [c.getIntVal() for c in hand]
    intVals.sort()
    for i in range(1,5):
        if(intVals[i]-1!=intVals[i-1]):
            return False,hand[4].getIntVal()
    return True,hand[4].getIntVal()

def checkRoyal(hand):
    intVals = [c.getIntVal() for c in hand]
    intVals.sort()
    if(intVals[0]==10):
        return checkStraight(hand)               
            
euler54()
        
