def aplha_ramp_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{chr(65+(i))}",end=" ")
        print()

if __name__ == '__main__':
    aplha_ramp_pattern(5)