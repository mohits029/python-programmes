n= int(input("Enter n value: "))
lst= []
x=1
num= 2
temp=2
flag= True

while x<=n:
    while num > temp:
        if num%temp==0:
            flag= False
            break
        temp+=1



    if flag==True:
        lst.append(num)
        x+=1
    temp=2
    flag=True
    num+=1

print(lst)


