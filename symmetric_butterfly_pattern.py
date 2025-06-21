def symmetric_butterfly_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for j in range(2*(n-i-1)):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
    # Bottom half
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            print("*", end="")
        for j in range(2 * (n - i - 1)):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print()

if __name__ == '__main__':
    symmetric_butterfly_pattern(5)
