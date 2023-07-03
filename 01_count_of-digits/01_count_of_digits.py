def count(n):
    count = 0
    while (n>0):
        n = int (n/10)
        count = count + 1
    return count

if __name__=="__main__":
    print(count(12345))