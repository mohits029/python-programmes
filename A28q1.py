l1= [12,3,8.3,'ram',True]
i=0
l2= []
while i< len(l1):
    if type(l1[i])== int:
        l2.append(l1[i])
    i+=1
print(l2)