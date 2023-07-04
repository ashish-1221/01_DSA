"""Function to generate factorial of a number"""
def fact(num):
    sum=1
    while(num>0):
        sum = sum*num
        num-=1
    return sum
if __name__=="__main__":
    print(fact(5))
    
    
    