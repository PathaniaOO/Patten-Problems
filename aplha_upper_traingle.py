def aphla_upper_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print(chr(65+j),end=" ")
        for j in range(i-1,-1,-1):
            print(chr(65+j),end=" ")

        print()

if __name__ == '__main__':
    aphla_upper_triangle(5)