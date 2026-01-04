a = int(input("Enter a number "))


for i in range(a):
    for j in range(i+1):
        print("*", end="")
    print("\n") 
for i in range(a):
    for j in range(i+1):
        print(j+1, end=" ")
        
    print("\n") 
for i in range(a):
    for j in range(i+1):
        print(i, end=" ")
    print()
 
   
for i in range(a):
    for j in range(a-i):
        print("*",end="")
    print()
for i in range(a):
    for j in range(a-i):
        print(j,end="")
    print()
        
    
for i in range(a):
    for j in range(a-i+1):
        print(" ",end=" ")
    for j in range((i*2)+1):
        print("*",end=" ")
    for j in range(a-i-1):
        print(" ",end="")
    print()
print() 
print() 
for i in range(a):
    for j in range(i+2):
        print(" ",end=" ")
    for j in range(((a-i)*2)-1):
        print("*",end=" ")
    for j in range(i-1):
        print(" ",end="")
    print()
    
print()
print()

for i in range(a):
    for j in range(a-i+1):
        print(" ",end=" ")
    for j in range((i*2)+1):
        print("*",end=" ")
    for j in range(a-i-1):
        print(" ",end="")
    print()
for i in range(a):
    for j in range(i+2):
        print(" ",end=" ")
    for j in range(((a-i)*2)-1):
        print("*",end=" ")
    for j in range(i-1):
        print(" ",end="")
    print()
    
    
print()
print()

for i in range(a):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(a):
    for j in range(a-i):
        print("*", end=" ")
    print()