def alpha_triangle_pattern(n):
    for i in range(n):
        for j in range(69-i,70,-1):
            print(chr(j),end=" ")
        print()
if __name__ == '__main__':
    alpha_triangle_pattern(5)

# ---------------------------------------------------------

# def alpha_triangle_pattern(n):
#     for i in range(n):
#         for j in range(69,69-i-1,-1):
#             print(chr(j),end=" ")
#         print()
# if __name__ == '__main__':
#     alpha_triangle_pattern(5)
#
# E
# E D
# E D C
# E D C B
# E D C B A