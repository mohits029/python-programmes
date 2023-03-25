lst= [1,22,0,9,-4,90,-22,3,0]
lstPositive=[]
lstnonpositive=[]
for i in lst:
    if i>0:
        lstPositive.append(i)
    else:
        lstnonpositive.append(i)



print(lst)
print(lstPositive)
print(lstnonpositive)