def letter_left_inverted_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print(f"{chr(65+j)}",end=" ")
        print()
if __name__ == '__main__':
    letter_left_inverted_triangle(5)
