'''
Created on Apr 1, 2015

@author: michael.simmarano
'''
import math
import EulerLib
import PrimeHelper

def Euler56():
    print("fdg")

def naivePow(a,b):
    curr = a
    for i in range(1,b):
        curr*=a
    return curr
    
def naiveExpDigSum(a,b):
    num = str(naivePow(a, b))
    currSum = 0
    for d in num:
        currSum+=int(d)
    return currSum, num

def investigate():
    highestSum = 0
    highestNum = ""
    highestA = 1
    highestB = 1
    for a in range(1,99):
        for b in range(1,99):
            currSum, theNumber = naiveExpDigSum(a, b)
            if(currSum>highestSum):
                highestSum = currSum
                highestNum = theNumber
                highestA = a
                highestB = b
    print(highestSum)
    print(highestNum)
    print(highestA)
    print(highestB)
    return highestSum, highestA, highestB
    #print("a = "+str(i)+" b = "+str(pow)+" : digSum: "+str(naiveExpDigSum(i, pow)))
        
investigate()