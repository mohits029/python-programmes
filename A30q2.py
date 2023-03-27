s1= {"Rohit Sharma", "Virat Kolhi", "KL Rahul","MS Dohni","Hardik Pandya"}
x=0
for i in s1:
    x+=1
    for j in list(s1)[x::]:
        print( i, j)