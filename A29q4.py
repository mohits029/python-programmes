l1=[]
s1= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in s1:
    l1.append((i,ord(i)))

print(l1)

sum=0
t1= (12,3,12,4,54,6,7,9,5,34,2,34,4,22,23,64)    
for i in t1:
    if i%2==0:
        sum+=i

print(sum)