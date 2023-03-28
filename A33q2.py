def sum(n):
    # bace case
    if n==0:
        return 0
    else:
        s= n+ sum(n-1)
        return s




print(sum(5))