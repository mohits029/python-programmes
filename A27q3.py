s= input("Enter a string: ")
l1= s.split()

max=0

for i in l1:
    if max < len(i):
        max= len(i)

print(max)