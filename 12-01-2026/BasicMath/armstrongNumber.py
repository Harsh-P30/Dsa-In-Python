#  Armstrong Number is a number that multiple each digit to it self n times where n is total digit count. 
# Ex 371 , count = 3
    # 3*3*3 + 7*7*7 + 1*1*1
    # 27    +   343 +   1 = 371 so it is a armstrong number

# Approach:- 
    # first count number of digits
    # get one by one all digits and calculate power in respect to count and add all result 
    # after getting result compare to actual values.
    
# Notes- 
    # to count lenth of any number first convert into string and use len()
    # to calculate power use ** 
  
def armstrongnumber(n):
    count = len(str(n)) # to calculate number of digits.
    val =0 
    copyN = n
    while n > 0:
        digit = n%10
        val = val +(digit**count) 
        n = n//10
    if(copyN==val):
        print(True)
    else:
        print(False)
armstrongnumber(153)