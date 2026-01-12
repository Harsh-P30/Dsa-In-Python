n = int(input("Enter a number "))

a=0
sign = 1
if n<0:
    sign = -1
    n=abs(n) # for absolute value / to remove sign
    
while n>0:
    b=n%10
    a=a*10+b
    n=n//10
    
print(a*sign)