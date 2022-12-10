def sol(matrix):
    sum = 0
    if matrix(0, 0):
        return 1
    else:
        sum = 0
        for i in range(1, "biggest square top left"):
            sum += sol(matrix - i*i)
            i += 1
            return sum

def 


