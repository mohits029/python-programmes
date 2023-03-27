s1= ["doctor","principle","computer","graphic","mohit","mumbai","dancer","dorimon","character","pineapple","break","breakup","Apple","aar"]
mylist= []
temp=[]
lc_alpha= 'abcdefghijklmnopqrstuvwxyz'
uc_alpha= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(0,26):
    for j in s1:
        if j.startswith(lc_alpha[i]) or j.startswith(uc_alpha[i]):
            temp.append(j)
    
    if len(temp)>0:
        mylist.append( tuple(temp) )
        temp.clear()

print(mylist)

  