x= "mohitsarkar"
print(x.isalpha())

a= 'mohi'

print(a in x)

vowels= 'aeiouAEIOU'

count=0

for i in x:
    if i in vowels:
        count+=1
print(count)

y= x[ ::-1]
print(y)

str1= "mohit sarkar     is my best friend hello, wolrd      mm thankyou so much     "

lst1= str1.split()

print(len(lst1))
