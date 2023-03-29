def sumodd(n):
    if n==1:
        return 1
    
    else:
        s= (n*2-1) + sumodd(n-1)
        return s

print(sumodd(10))