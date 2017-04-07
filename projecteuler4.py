a = [100, 999]
b = [100, 999]
zahl = 0

n = 997799

def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1
    
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True
#print(isPalindrome(n))   

def palindromeproduct(n):
    while n > 10000:
        if isPalindrome(str(n)) == True:
            print(str(n) + "is a palindrome")
            for i in range(101,1000):
                if n%i==0 and n/i<1000:
                    print("n = " + str(i) + "*" + str(int(n/i)))
                    print("n= " + str(n))
                    return
        n=n-1
        
palindromeproduct(997799)
