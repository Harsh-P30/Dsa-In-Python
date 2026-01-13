# for(int i=0;i<7;i++){
#     print(i)
# }

#cant use this method in python its c method to use for loop

for i in range(6):  # range() is a funtion in python that return in sequence, start from 0 by default and increament by 1
    print(i)
  
print("\n")
    
for i in range(2,9):
    print(i)
    if(i==5):
        break #stop executing loop
    
print("\n")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
for a in range(4):
    for b in range(5):
        print(a,b)
        

for i in range(3):
    for j in range(3):
        print(i*3+j+1,end=" ")
    print()
    
i=1
while i<5:
    print(i)
    i+=1