print(sum([45,5,10,5,1]))

lst= [12,23,12,34,5]
n=len(lst)
print(sum(lst)/n)
print(n)


lst2=[]

for i in lst:
    lst2.append(i**2)

print(lst)
print(lst2)

print(sorted(lst,reverse=True))