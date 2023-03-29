def even(n):
    if n==1:
        print(n+1)
    else:
        print(n*2)
        even(n-1)
even(10)


def sq(n):
    if n==1:
        print(n**2)
    else:
        sq(n-1)
        print(n**2)
    
sq(10)