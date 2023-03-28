def odd(n):
    if n==1:
        print(n)
        return
    else:
        odd(n-1)
        
        print(2*n-1)




odd(13)

