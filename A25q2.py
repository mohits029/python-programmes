n= int(input("Enter n value: "))
lst= []
a,b=0,1
for i in range(n):
    c=a+b
    a=b
    b=c
    lst.append(c)

print(lst)