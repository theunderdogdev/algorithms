def calc_coeff():
    n = int(input("Enter the value of n:"))
    k = int(input("Enter the value of n:"))
    arr = [[0]*(n+1) for _ in range(n+1)]
    if n >= k >= 0 and n >= 0:
        for row in range(n+1):
            for col in range(n+1):
                if row == col or col == 0:
                    arr[row][col] = 1
                else:
                    arr[row][col] = arr[row-1][col] + arr[row-1][col-1]
                print(arr[row][col], end="\t") if arr[row][col] != 0 else print(end='\t')
            print('')
    else:
        print("invalid input")


if __name__ == "__main__":
    calc_coeff()
