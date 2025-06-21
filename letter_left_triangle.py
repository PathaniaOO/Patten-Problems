def letter_left_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{chr(65+j)}",end=" ")
        print()
if __name__ == '__main__':
    letter_left_triangle(5)
