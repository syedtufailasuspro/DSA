n = int(input()) # 5
m = int(input()) # 4 

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
]

for i in range(n+m - 1): #0 1 2 ..  7
    if i <n: #0 1 2 3 4 
        row = i
        column = 0
    else:
        row = n - 1 # 4
        column = i - row # 1 2 3

    while row >=0 and column < m:
        print(matrix[row][column] ,end = " ")
        row -= 1
        column += 1
        