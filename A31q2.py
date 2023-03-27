d1= {1:"Mohit", 8:"Sumit", 2:"Priya", 3:"Jeetu", 10:"Rajni",6:"Priyanka"}
d2={}
key= sorted(d1)

for i in key:
    # temp= d1[i]
    d2[i]= d1[i]

d1= d2
print(d1)
del d2

