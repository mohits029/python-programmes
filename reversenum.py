def rev(n):
    if n==0:
        return 0
    else:
        print(n%10)
        rev(n//10)

rev(127783)