def isEven(x):
    if x%2==0:
        return True
    else:
        return False
    

def grater(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    

def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
        
    else:
        return True
        
 

print(isPrime(13))