import math

def eval1(p):
    x = p[0]
    y = p[1]
    return 2*x*(math.e**(x**2+y**2))+1

def eval2(p):
    x = p[0]
    y = p[1]
    return 2*y*(math.e**(x**2+y**2)) + 5

def eval3(p):
    return p[0] + 2*p[1] + 4*math.sqrt(1+p[0]**2+p[1]**2)


def extremum_by_coordinate(evallist):
    speed = 0.1
    x = [0, 0]
    xn = [0,0]
    d = 10
    while abs(d) > 10**-6:
        d = 0
        for i in range(len(x)):
            xn[i] = x[i] - speed * evallist[i](x)
            d += xn[i]**2 - x[i]**2
            x[i] = xn[i]
    return xn

def bin_minimization(eval, grad, x):
    a = 0
    a_minus = []
    a_plus = []
    i = 0
    while True:
        a_minus.append(-a)
        a_plus.append(a)
        if (i >= 2):
            v1 = eval([x[0] - a_minus[i-2]*grad[0], x[1] - a_minus[i-2]*grad[1]])
            v2 = eval([x[0] - a_minus[i-1]*grad[0], x[1] - a_minus[i-1]*grad[1]])
            v3 = eval([x[0] - a_minus[i]*grad[0], x[1] - a_minus[i]*grad[1]])
            if (v2 <= v1 and v2 <= v3):
                f = -1
                break
            v1 = eval([x[0] - a_plus[i-2]*grad[0], x[1] - a_plus[i-2]*grad[1]])
            v2 = eval([x[0] - a_plus[i-1]*grad[0], x[1] - a_plus[i-1]*grad[1]])
            v3 = eval([x[0] - a_plus[i]*grad[0], x[1] - a_plus[i]*grad[1]])
            if (v2 <= v1 and v2 <= v3):
                f = 1
                break
        a += 0.1
        i += 1
    if (f == -1):
        al = a_minus[i]
        ar = a_minus[i-2]
    else:
        al = a_plus[i-2]
        ar = a_plus[i]
    
    e = 10**-6
    while abs((al - ar)) > e:
        a = (al+ar) / 2
        a1 = (al + ar-e)/2
        a2 = (al+ar+e)/2
        v1 = eval([x[0] - a1*grad[0], x[1] - a1*grad[1]])
        v2 = eval([x[0] - a2*grad[0], x[1] - a2*grad[1]])
        if (v1 < v2):
            al = a
        else:
            ar = a
    return a

def get_grad(p, eval):
    grad = []
    for i in range(len(p)):
        pn = []
        for j in range(len(p)):
            pn.append(p[j])
        pn[i] += 10**-10
        grad.append((eval(pn)-eval(p))*10**10)
    return grad

def quickest_decent(eval):
    speed = 0.1
    x = [0, 0]
    xn = [0, 0]
    d = 1
    while abs(d) > 10**-6:
        grad = get_grad(x, eval)
        speed = bin_minimization(eval, grad, x)
        d = 0
        for i in range(len(x)):
            xn[i] = x[i] - speed * grad[i]
            d += xn[i]**2 - x[i]**2
            x[i] = xn[i]
    return x


        
        

print(extremum_by_coordinate([eval1, eval2]))
print(quickest_decent(eval3))