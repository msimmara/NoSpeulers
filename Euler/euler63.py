import math

def euler63():
    
    total = 0  
    
    
    for currN in range(1,22):
        for currP in range(1,10):
            currPowered = (int(math.pow(currP,currN)))
            if(len(str(currPowered))==currN):
                total+=1
                
    print(total)
    
    
    
    

euler63()