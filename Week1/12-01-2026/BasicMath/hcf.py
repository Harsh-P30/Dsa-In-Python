def hcf(a,b):
    while b>0:
        a=a%b
        c=a
        a=b
        b=c
    return a
        
    
n = int(input("Enter a number "))
m = int(input("Enter a number "))

print(hcf(n,m))


def hcf1(a,b):
    if(b==0):
        return a
    hcf1(b,a%b)
    
print(hcf1(474,4))