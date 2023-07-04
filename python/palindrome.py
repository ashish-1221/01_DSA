"""Module String"""
def palindrome (num):
    """Function for checking whether a number is palindrome or not"""    
    rev=0
    digit=0
    num1=num
    while (num1!=0):
        digit = int(num1%10)
        rev = rev*10+digit
        num1 = int(num1/10)
    if num==rev:
        return True
    else:
        return False
        
    
if __name__=="__main__":
    print(palindrome(123321))