a= "Mohit 505 hello 1 world x 65"
l2=a.split()
print(l2)
l3=[]

for i in l2:
    try:
        l3.append(float(i))
    except:
        pass

print(l3)