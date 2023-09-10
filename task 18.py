def find_max_min_sum(matrix):
    n = len(matrix)
    max_sum = [[0] * n for _ in range(n)]
    min_sum = [[0] * n for _ in range(n)]
    max_sum[0][0] = min_sum[0][0] = matrix[0][0]

    for j in range(1, n):
        max_sum[0][j] = max_sum[0][j-1] + matrix[0][j]
        min_sum[0][j] = min_sum[0][j-1] + matrix[0][j]

    for i in range(1, n):
        max_sum[i][0] = max_sum[i-1][0] + matrix[i][0]
        min_sum[i][0] = min_sum[i-1][0] + matrix[i][0]

    for i in range(1, n):
        for j in range(1, n):
            max_sum[i][j] = max(max_sum[i-1][j], max_sum[i][j-1]) + matrix[i][j]
            min_sum[i][j] = min(min_sum[i-1][j], min_sum[i][j-1]) + matrix[i][j]
            
    return max_sum[n-1][n-1], min_sum[n-1][n-1]

# Матрица с монетами
matrix = [
    [85, 30, 85, 73, 23, 44, 52, 78, 100, 91],
    [80, 47, 13, 17, 54, 30, 99, 92, 15, 51],
    [43, 67, 44, 15, 18, 48, 35, 6, 70, 37],
    [48, 22, 49, 29, 29, 61, 18, 18, 69, 48],
    [19, 81, 70, 50, 16, 3, 66, 29, 88, 58],
    [96, 74, 20, 49, 12, 2, 95, 100, 71, 96],
    [20, 39, 91, 65, 4, 88, 26, 25, 76, 33],
    [67, 53, 71, 73, 17, 9, 31, 90, 67, 50],
    [81, 3, 71, 34, 60, 56, 92, 89, 45, 72],
    [15, 55, 24, 2, 96, 85, 76, 8, 30, 55]
]

max_sum, min_sum = find_max_min_sum(matrix)
print(max_sum, min_sum)
