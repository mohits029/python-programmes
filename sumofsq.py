def sqsum(n):
    if n==1:
        return 1
    else:
        s= n**2 + sqsum(n-1)
        return s
    
print(sqsum(5))