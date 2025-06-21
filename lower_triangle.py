# def lower_triangle(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ",end=" ")
#         for j in range(i,n):
#             print("*",end=" ")
#         for j in range(i,n-1):
#             print("*",end=" ")
#         print()
# if __name__ == '__main__':
#     lower_triangle(5)

# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

def lower_triangle(n):
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()
if __name__ == '__main__':
    lower_triangle(5)
