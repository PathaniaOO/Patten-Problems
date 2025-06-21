def diamond(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()
    for i in range(n-2,-1,-1):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()
if __name__ == '__main__':
    diamond(5)