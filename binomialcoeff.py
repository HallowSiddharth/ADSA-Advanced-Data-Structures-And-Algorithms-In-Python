def binomialCoeff(n, k):
    table = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if i == 0 or j == 0 or i == j:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j] + table[i - 1][j - 1]
    return table[n][k]


print(binomialCoeff(4, 2))
