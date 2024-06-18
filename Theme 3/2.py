import math
b = 9999
a = 0

def eval(x):
    return (math.e**(-2*x)*math.sin(9*x))

def rectangle():
    sigma = 0
    for i in range(4, 9):
        N = 10**i
        psigma = sigma
        sigma = 0
        h = (b-a) / N
        x = a
        for _ in range(1, N):
            sigma += eval((x+x+h)/2)
            x += h
        sigma *= h
        if (abs(sigma - psigma) < 10**-6):
            return sigma
        print(sigma)

def trapezoid():
    sigma = 0
    for i in range(4, 9):
        N = 10**i
        psigma = sigma
        sigma = 0
        h = (b-a) / N
        x = a+h
        for _ in range(1, N):
            sigma += eval(x)
            x += h
        sigma += 1/2 * (eval(a) + eval(b))
        sigma *= h
        if (abs(sigma - psigma) < 10**-6):
            return sigma
        print(sigma)
    
def parabola():
    sigma = 0
    for i in range(4, 9):
        N = 10**i
        psigma = sigma
        sigma = 0
        h = (b-a) / N
        x = a+h
        
        for _ in range(1, int(N/2)):
            sigma += 4*eval(x)
            sigma += 2*eval(x+h)
            x += h*2
        sigma += (eval(a) + eval(b))
        sigma *= h/3
        if (abs(sigma - psigma) < 10**-6):
            return sigma
        print(sigma)

s = rectangle()
print(s)