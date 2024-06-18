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
        B.append(matrix[i][len(matrix[i])-1])
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


def cubic_spline_generator(points):
    n = len(points[0])-1
    a = []
    b = []
    d = []
    h = 1
    for i in range(n):
        a.append(points[1][i])
        b.append(0)
        d.append(0)
    tmp=[]

    for i in range(0, n-1):
        tmp.append([])
        for j in range(n):
            if (j >= i-1 and j <= i+1 ):
                if (j == i):
                    tmp[i].append(4*h)
                else:
                    tmp[i].append(h)
            else:
                tmp[i].append(0)
        k = 3*((points[1][i+2]-points[1][i+1])/h - (points[1][i+1] - points[1][i])/h)

        tmp[i].append(k)
    
    c = Shuttle_methode(tmp)
    t = [0]
    for i in c:
        t.append(i)
    c = t

    b[n-1] = ((points[1][n] - points[1][n-1])/h) - (2/3) * h * c[n-1]

    for i in range(n-2, 0, -1):
        b[i] = ((a[i+1]) - a[i]/h) - (1/3) * h * (c[i+1]+ 2 * c[i])
    
    b[0] = ((a[1]) - a[0]/h) - (1/3) * h * (c[1])
    
    for i in range(n-1):
        d[i] = (c[i+1] - c[i])/(3*h)
    
    d[n-1] = (-1 * c[n-1])/(3 * h)

    return([a, b, c, d])

def spline_to_desmos(p, s):
    a = s[0]
    b = s[1]
    c = s[2]
    d = s[3]
    for i in range(len(s[0])):
        print(f"y={a[i]}+{b[i]}*(x-{p[0][i]})+{c[i]}*(x-{p[0][i]})^2+{d[i]}*(x-{p[0][i]})^3   {{{p[0][i]}<=x<={p[0][i+1]}}}")

def eval_spline(x, p, s):
    a = s[0]
    b = s[1]
    c = s[2]
    d = s[3]
    r = 0
    for i in range(len(p[0])-1):
        if (x > p[0][i] and x < p[0][i+1]):
            r = i
            break
    y = a[i] + b[i]*(x-p[0][i])+c[i]*(x-p[0][i])**2+d[i]*(x-p[0][i])**3
    return y

def Lagrange_polynom_generator(points):
    c = []
    n = len(points[0])
    for i in range(n):
        t = 1
        for j in range(n):
            if (i != j):
                t /= (points[0][i] - points[0][j])
        c.append(t)
    return c

def Lagrange_polynom_evaluate(points, coefficients, x):
    c = coefficients
    m = points
    s = 0
    for i in range(len(c)):
        l = c[i]
        for j in range(len(c)):
            if (i != j):
                l *= (x - m[0][j])
        s += m[1][i] * l
    return s

matrix = [[0, 1, 2, 3, 4], [0, 0.5, 0.86603, 1, 0.86603]]
matrix2 = [[0.1*math.pi, 0.2*math.pi, 0.3*math.pi, 0.4*math.pi], [math.sin(0.1*math.pi),math.sin(0.2*math.pi),math.sin(0.3*math.pi),math.sin(0.4*math.pi)]]

coef = Lagrange_polynom_generator(matrix2)

v = Lagrange_polynom_evaluate(matrix2, coef, (0.25*math.pi))
print(math.sin(0.25*math.pi)-v)