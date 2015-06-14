import EulerLib
import PrimeHelper

PH = PrimeHelper.PrimeHelper()

#2(x^2) +(N^2) - (xN)^2  -  2(r^2) = (n^2-2)y^2

def checkForX(x,N):
    numerator = 2*(x*x)+(N*N) - (x*N)*(x*N)  -  N*N/2
    print(numerator)
    denominator = N*N-2
    print(denominator)
    print(numerator/denominator)
    if(numerator%denominator!=0):
        return False

    return EulerLib.isSquareNumber(int(numerator/denominator))
