def binary_no_triangle(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j) % 2==0:
                print(f"1", end=" ")
            else:
                print(f"0", end=" ")
        print()
if __name__ == '__main__':
    binary_no_triangle(5)