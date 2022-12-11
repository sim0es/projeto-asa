# def sol(matrix):
#     sum = 0
#     if matrix(0, 0):
#         return 1
#     else:
#         sum = 0
#         for i in range(1, "biggest square top left"):
#             sum += sol(matrix - i*i)
#             i += 1
#             return sum

matrix = []
i = 0
linha_final = int(input('n linhas: '))
coluna_final = int(input('n colunas: '))

linha_atual = 0
coluna_atual = 0

while linha_atual < linha_final:
    linha_campo = []
    while coluna_atual < coluna_final:
        linha_campo += [0]
        coluna_atual += 1
    matrix += [linha_campo]
    coluna_atual = 0
    linha_atual += 1

print(matrix)

counter = 0

while counter < linha_final:
    c = int(input('Valor de c: '))
    if c != 0:    
        matrix[counter][c - 1] = 1
        d = c
        while d > 0:
            matrix[counter][d - 1] = 1
            d -= 1
    counter += 1

print(matrix)

def countSquares(self, A):
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return sum(map(sum, A))

print(countSquares(0, matrix))