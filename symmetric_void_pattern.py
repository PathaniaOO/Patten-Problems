def symmetric_void_pattern(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end="")
        for j in range(2*i):
            print(" ",end="")
        for j in range(i,n):
            print("*",end="")
        print()
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for j in range(2*(n-i-1)):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
if __name__ == '__main__':
    symmetric_void_pattern(5)