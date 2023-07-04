"""Function to generate factorial of a number"""
def fact(num):
    """Function to print factorial of a number"""
    sum1=1
    while(num>0):
        sum1 = sum1*num
        num-=1
    return sum1
if __name__=="__main__":
    print(fact(5))
    
    
    