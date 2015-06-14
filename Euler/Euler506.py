import math

def simpleModularExponentiation(n,e,mod):
    currModded = 1
    for i in range(1,e):
        currModded*=n
        currModded=currModded%mod
    return currModded
    
def newSumN(n,mod):
    baseString= "123432"
    currentString = ""+baseString
    currN=1
    theSum=0
    baseStart=0
    modDigits = int(math.log10(mod)+1)
    for i in range(1,n+1):
        vInit = ""
        vFinal = ""
        currentSum = 0
        currentRepeats = 0
        #initial
        for j in range(baseStart,6):
            curChar = baseString[j]
            vInit+=curChar
            currentSum+=int(curChar)
            if(currentSum==i):
                baseStart=(j+1)%6
                break
        #middle
        amountLeft = i-currentSum
        currentRepeats = int(amountLeft/15)
        currentSum+=(currentRepeats*15)
        #end
        if(currentSum<i):
            for j in range(0,6):
                curChar = baseString[j]
                vFinal+=curChar
                currentSum+=int(curChar)
                if(currentSum==i):
                    baseStart=(j+1)%6
                    break
        initDigits = len(vInit)
        middleDigits = currentRepeats*6
        finalDigits = len(vFinal)
        #coef = int(math.pow(10,middleDigits+finalDigits))
        coef=1
        for i in range(0,middleDigits+finalDigits):
            coef*=1000000
        initVCalc = (int("0"+vInit)*(coef))%mod
        finalVCalc = (int("0"+vFinal))%mod
        middleCalc = 0
        currMul = 1
        for x in range(1,currentRepeats+1):
            currMul*=10
            middleCalc+=(currMul*123432)%mod
            middleCalc=middleCalc%mod
        theSum+=initVCalc+finalVCalc+middleCalc
        theSum=theSum%mod
        print(theSum)
        if(theSum==1 and i!=1):
            print("Repeat at: "+str(i))
            break

def SumN(n,mod):
    baseString = "123432"
    currString = ""+baseString
    currN=1
    theSum = 0
    for i in range(1,n+1):
            currSum = 0
            currV = ""
            while(currSum<currN):
                    if(len(currString)==0):
                            #sumLeft = currN-currSum
                            #baseRepeats = int(sumLeft/15)
                            #currSum+=baseRepeats*15
                            #if(currSum>=currN):
                            # break
                            currString=currString+baseString
                    currAdd = int(currString[0])
                    currV = currV+str(currAdd)
                    currString = currString[1:]
                    currSum=currSum+currAdd
            theSum+=int(currV)%mod
            theSum = (theSum)%mod
            currN+=1
            
            print ("S("+str(currN-1)+") modded: "+str(theSum))
            #print ("V("+str(currN-1)+") modded: "+str(int(currV)%mod))
            
    return theSum

def Euler506():
    result = {}
    N3 = simpleModularExponentiation(10,4,3)
    N337 = simpleModularExponentiation(10,4,337)
    N12211 = simpleModularExponentiation(10,4,12211)
    S3 = SumN(N3)
    S337 = SumN(N337)
    S12211 = SumN(N12211)
    result["N3"] = N3
    result["N337"] = N337
    result["N12211"] = N12211
    result["S3"] = S3
    result["S337"] = S337
    result["S12211"] = S12211
    return result
     


def Euler506_ORIG():
    baseString = "123432"
    currString = ""+baseString
    currN=1
    theSum = 0
        
    for i in range(0,340):
            currSum = 0
            currV = ""
            while(currSum<currN):
                    if(len(currString)==0):
                            currString=currString+baseString
                    currAdd = int(currString[0])
                    currV = currV+str(currAdd)
                    currString = currString[1:]
                    currSum=currSum+currAdd
            #theSum=theSum+currSum
            currN+=1
            #print ("Current N: "+str(currN)+" V(n): "+currV+" S(n) modded: "+str(theSum%123454321))
            #print ("S(n) modded: "+str(theSum%123454321))
            #print ("S("+str(currN-1)+") modded: "+str(theSum%3))
            #print ("S("+str(currN-1)+") modded: "+str(theSum%337))
            #print ("S("+str(currN-1)+") modded: "+str(theSum%12211))

#Euler506()

# Guess: S(n) mod 123454321 = S(n mod 3) + S(n mod 337) +S(n mod 12211)