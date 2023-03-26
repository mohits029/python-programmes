l1= [10,10,16,52,1,6,16,52,5,52,40,50,20,40,40,50,20]
s= set()

for i in l1:
    s.add(i)

for i in s:
    print (i, "count= ", l1.count(i))