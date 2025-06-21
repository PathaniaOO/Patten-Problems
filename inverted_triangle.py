# def inverted_triangle(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end=" ")
#         print()
# if __name__ == '__main__':
#     inverted_triangle(5)
#
# -------------OUTPUT--------------
# * * * * *
# * * * *
# * * *
# * *
# *


# def inverted_triangle(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print(f"{j+1}",end=" ")
#         print()
# if __name__ == '__main__':
#     inverted_triangle(5)
# ------OUTPUT----
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# def inverted_triangle(n):
#     for i in range(n,0,-1):
#         for j in range(i,0,-1):
#             print(f"{chr(97+j)}",end=" ")
#         print()
# if __name__ == '__main__':
#     inverted_triangle(5)
#
# ------output---------
# f e d c b 
# e d c b
# d c b
# c b
# b