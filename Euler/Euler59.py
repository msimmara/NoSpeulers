import EulerLib
import PrimeHelper
import math
from operator import itemgetter
from _codecs import decode
from nt import system

def xorEncode(value,key):
    xB = bytes(value,"ASCII")
    yB = bytes(key,"ASCII")
    lengthV = len(value)
    lengthK = len(key)
    result = ""
    
    for i in range(0,lengthV):
        result+=chr(xB[i]^yB[i%lengthK])
         
    return result

def readCipher():
    ciph = open("C:\\Users\\michael.simmarano\\workspace\\Euler\\cipher59.txt")
    ciphNums = ciph.readline().split(",")
    ciphStr = ""
    for i in ciphNums:
        ciphStr+=chr(int(i))
    return ciphStr

print(readCipher())
    
def euler59():
    #97 - 122 inclusive
    encrypted = readCipher()
    currPassInts = [97,97,97]
    answered = "n"
    originalText=""
    while answered!="y":
        currPasswordGuess = chr(currPassInts[0])+chr(currPassInts[1])+chr(currPassInts[2])
        currGuess = xorEncode(encrypted, currPasswordGuess)
        if("the" in currGuess and "Gospel" in currGuess):
            print("Current password: "+currPasswordGuess)
            print(currGuess)
            answered = input("Enter y if correct...")
            if(answered=="y"):
                originalText = currGuess
                break
        currPassInts[2]+=1
        if(currPassInts[2]>122):
            currPassInts[2]=97
            currPassInts[1]+=1
        if(currPassInts[1]>122):
            currPassInts[1]=97
            currPassInts[0]+=1
        if(currPassInts[0]>122):
            print("failed")
            return
        
    theSum = 0
    for c in originalText:
        theSum+=ord(c)
    print(theSum)

euler59()
    