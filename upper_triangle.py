def upper_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()
if __name__ == '__main__':
    upper_triangle(5)

