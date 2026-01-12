def PalindromeNumber(a):
    original = a
    if a<0:
        return 0
    print(a)
    rev = 0
    while a>0:
        n=a%10
        rev=rev*10+n
        a=a//10
    print(rev) 
    return original == rev
    
    
    
ans = PalindromeNumber(int(input("Enter a number to check palindrome ")))
print(bool(ans))