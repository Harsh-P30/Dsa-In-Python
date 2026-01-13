# "/" and "//" both used to divide but "/" gives result in float and "//" in integer ex 10/3= 3.33333 and 10//3=3(nearest number(round off))
# count number of digit like a in 789654 has 6 digits     

# Approach 
    # apply a while till the value > 0 
    # divide by 10 to elemenate last digit
    # and count the iteration


a = int(input("Enter a number "))

count=0
while a>0:
    a=a//10
    count=count+1    
print(count)