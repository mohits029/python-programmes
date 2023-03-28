p= float(input("Enter principle: "))
r= float(input("Enter rate: "))
t= float(input("Enter time: "))

def ci(p,r,t):
    x= p* ((1+ (r/100))**t)
    x= x-p
    return x


x= ci(p,r,t)
print(x)