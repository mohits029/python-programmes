l1=["America","Uttarakhand","London","Germany","Afganistan","Nepal","America", "Nepal"]
# l1.sort()
# print(l1)
i=0
c=1
for x in l1:
    if i== l1.index(x):
        if c== l1.count(x):
            pass
        else:
            print(x, "is repeate")
    i+=1
