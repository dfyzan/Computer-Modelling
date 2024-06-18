import math

#x, y = map(float, input("Введите количество коэффициентов в ширину и в высоту: ").split())

def substract(matrix, n, m, k): #Возвращает матрицу, где из строки m вычли строку n*k
    y = len(matrix)
    x = len(matrix[0])
    for i in range(x):
        matrix[m][i] -= matrix[n][i] * k
    return matrix

def Gauss(matrix):
    y = len(matrix)
    x = len(matrix[0])
    for ix in range (x-1):
        for iy in range(y):
            if (ix != iy and matrix[ix][ix] != 0):
                matrix = substract(matrix, ix, iy, matrix[iy][ix]/matrix[ix][ix])
    xarr = []
    for ix in range(x-1):
        if (matrix[ix][ix] != 0):
            xarr.append(matrix[ix][y]/matrix[ix][ix])
        else:
            xarr.append("NaN")
    return xarr

def antimatr(matrix):
    anti = []
    for i in range(len(matrix)):
        anti.append([])
        for j in range(len(matrix)):
            if (i == j):
                anti[i].append(1/matrix[i][i])
            else:
                anti[i].append(0)
    return anti

def identity(matrix):
    identity = []
    for i in range(len(matrix)):
        identity.append([])
        for j in range(len(matrix)):
            if (i == j):
                identity[i].append(1)
            else:
                identity[i].append(0)
    return identity

def matrix_mult(m1, m2):
    m = []
    l = len(m1)
    for i in range(l):
        m.append([])
        for j in range(l):
            s = 0
            for k in range(l):
                s += m1[i][k] * m2[k][j]
            m[i].append(s)
    return m

def matrix_sub(m1, m2):
    m = []
    l = len(m1)
    for i in range(l):
        m.append([])
        for j in range(l):
            m[i].append(m1[i][j] - m2[i][j])
    return m

def matrix_add(m1, m2):
    m = []
    l = len(m1)
    for i in range(l):
        m.append([])
        for j in range(l):
            m[i].append(m1[i][j] + m2[i][j])
    return m

def vector_add(m1, m2):
    m = []
    l = len(m1)
    for i in range(l):
            m.append(m1[i] + m2[i])
    return m

def vector_sub(m1, m2):
    m = []
    l = len(m1)
    for i in range(l):
            m.append(m1[i] - m2[i])
    return m

def matrix_mult_vec(m, v):
    mat = []
    l = len(m)
    for i in range(l):
        s = 0
        for k in range(l):
            s += m[i][k] * v[k]
        mat.append(s)
    return mat

def vector_length(v):
    s = 0
    for i in v:
        s += i**2
    return math.sqrt(s)

def Jacobi(matrix):
    xarr = []
    x1 = []

    A = []
    B = []
    for i in range(len(matrix)):
        A.append([])
        B.append(matrix[i][len(matrix)])
        for j in range(len(matrix)):
            A[i].append(matrix[i][j])
    

    for i in range(len(matrix)):
        xarr.append(B[i]/A[i][i])
        x1.append(0)
    D = antimatr(matrix)
    I = identity(matrix)

    while (True):
        x1 = vector_add(matrix_mult_vec(matrix_sub(I, (matrix_mult(D, A))), xarr), matrix_mult_vec(D, B))
        if (vector_length(matrix_mult_vec(A, xarr)) < 10 ** -6 or x1 == xarr):
            break
        xarr = x1
        

    return xarr

def Seidel(matrix):
    xarr = []
    x1 = []

    A = []
    B = []
    for i in range(len(matrix)):
        A.append([])
        B.append(matrix[i][len(matrix)])
        for j in range(len(matrix)):
            A[i].append(matrix[i][j])
    

    for i in range(len(matrix)):
        xarr.append(B[i]/A[i][i])
        x1.append(B[i]/A[i][i]+10)

    while (True):
        for i in range(len(matrix)):
            s = 0
            for j in range(0, len(matrix)):
                if (i != j):
                    s += (-1*(A[i][j]/A[i][i]))*x1[j]
            s += (B[i]/A[i][i])
            x1[i] = s
            
        if (vector_length(vector_sub(matrix_mult_vec(A, xarr), B)) < (10 ** -2) or x1 == xarr):
            break
        for i in range(len(x1)):
            xarr[i] = x1[i]
        

    return xarr

def minor(matrix, x, y = 0):
    m = []
    l = len(matrix)
    if (l == 2 and x == 0):
        return [matrix[1][1]]
    elif (l == 2 and x == 1):
        return [matrix[1][0]]
    for i in range(0, l):
        if (i != y):
            m.append([])
            for j in range(l):
                if (i < y and j != x):
                    m[i].append(matrix[i][j])
                elif (i != 0 and j != x and y == 0 or j != x and i > y):
                    m[i-1].append(matrix[i][j])
    return m

def determinant(matrix):
    l = len(matrix)
    if (l == 1):
        return matrix[0]
    else:
        s = 0
        for i in range(l):
            s += matrix[0][i] * determinant(minor(matrix, i)) * ((-1) ** i)
    return s       

def substitute(matrix, v, x):
    m = []
    for i in range(len(matrix)):
        m.append([])
        for j in range(len(matrix)):
            m[i].append(matrix[i][j])
        m[i][x] = v[i]
    return m

def Cramer(matrix):
    A = []
    B = []

    for i in range(len(matrix)):
        A.append([])
        B.append(matrix[i][len(matrix)])
        for j in range(len(matrix)):
            A[i].append(matrix[i][j])

    D = determinant(A)
    xarr = []
    for i in range(len(matrix)):
        d = determinant(substitute(A, B, i))
        x = d/D
        xarr.append(x)
    return xarr

def transpose_matrix(matrix):
    m = []
    for i in range(len(matrix)):
        m.append([])
        for j in range(len(matrix)):
            m[i].append(0)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            m[i][j] = matrix[j][i]
    return m

def reverse_matrix(matrix):
    d = determinant(matrix)
    a = []
    for i in range(len(matrix)):
        a.append([])
        for j in range(len(matrix)):
            a[i].append((-1)**(i+j) * determinant(minor(matrix, j, i)))
            a[i][j] /= d
    t = transpose_matrix(a)
    return t

def Matrix_methode(matrix):
    A = []
    B = []

    for i in range(len(matrix)):
        A.append([])
        B.append(matrix[i][len(matrix)])
        for j in range(len(matrix)):
            A[i].append(matrix[i][j])
    
    R = reverse_matrix(A)
    xarr = matrix_mult_vec(R, B)
    return xarr

def Shuttle_methode(matrix):
    A = []
    B = []
    xarr = []

    for i in range(len(matrix)):
        A.append([])
        B.append(matrix[i][len(matrix)])
        xarr.append(0)
        for j in range(len(matrix)):
            A[i].append(matrix[i][j])
    

    for i in range(1, len(matrix)):
        A[i][i] = A[i][i] - ((A[i][i-1]/A[i-1][i-1])*A[i-1][i])
        B[i] = B[i] - ((A[i][i-1]/A[i-1][i-1])*B[i-1])

    xarr[len(matrix)-1] = B[len(matrix)-1]/A[len(matrix)-1][len(matrix)-1]
    for i in range(len(matrix)-2, -1, -1):
        xarr[i] = (B[i] - A[i][i+1]*xarr[i+1])/A[i][i]
    return xarr


matrix = []
#for i in range(y):
#    x = input(f"Введите {x} коэффициентов строки {(i+1)}: ").split()
#    matrix.append(x)

matrix1 = [[2, -7, 8, -4, 57], [0, -1, 4, -1, 24], [3, -4, 2, -1, 28], [-9, 1, -4, 6, 12]]
matrix2 = [[5,-2,5,2], [0, 2, 2, -1], [2, 2, 5, 0]]
matrix3 = [[-24,-6,4,7,130],[-8,21,4,-2,139],[6,6,16,0,-84],[-7,-7,5,24,-165]]
matrix4 = [[7, -5, 0, 0, 0,38],[-6, 19, -9, 0, 0,14],[0, 6, -18, 7, 0,-45],[0, 0, -7, -11, -2,30],[0,0,0,5,-7,48]]
print("Решение первой системы матричным методом и методом Гаусса:", Matrix_methode(matrix1), Gauss(matrix1), sep="\n")
print("Решение второй системы методом Крамера и Якоби:", Cramer(matrix2), Jacobi(matrix2), sep="\n")
print("Решение третьей системы методом Зейделя:", Seidel(matrix3), sep="\n")
print("Решение четвёртой системы методом прогонки:", Shuttle_methode(matrix4), sep="\n")