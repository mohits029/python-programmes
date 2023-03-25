temp=2
flag=True
for i in range(15,46):
    while temp<i:
        if i%temp== 0:
            flag=False
            break
        temp+=1


    if flag==True:
        print(i)
    temp=2
    flag=True
 


