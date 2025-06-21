# def number_pattern(n):
#     for i in range(n):
#         for j in range(n):
#             if i==0 or i==n-1 or j==0 or j==n-1:
#                 print(f"{4}", end=" ")
#             elif i==n-2 or i==1 or j==1 or j==n-2:
#                 print(f"{3}", end=" ")
#             elif i==n-3 or i==2 or j==2 or j==n-3:
#                 print(f"{2}", end=" ")
#             elif i == n - 4:
#                 print(f"{1}", end=" ")
#         print()
# if __name__ == '__main__':
#     number_pattern(7)
# --------------------------------------------------

def number_pattern(n):
    for i in range(n):
        for j in range(n):
            # Find the minimum distance from any border
            min_dist = min(i, j, n - i - 1, n - j - 1)
            # Calculate number: outermost layer is highest
            print(n//2 - min_dist + 1, end=" ")
        print()
if __name__ == '__main__':
    number_pattern(7)