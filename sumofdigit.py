def sumofdigit(n):
    if n==0:
        return 0
    else:
        s= n%10+ sumofdigit(n//10)
        return s

print(sumofdigit(345322))