l1= [1,23,4,2,4,4,5,5,23,3,1,434,3,4]
s= set(l1)
print(s)


even= set()
odd= set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)

print(even)
print(odd)