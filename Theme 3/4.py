import math

def calculation(x):
    k = 1
    sigma = 0
    psigma = -9999
    while(abs(sigma-psigma) > 10 ** (-6)):
        s = (-1)**k / (math.sin(k*x) + 9 + k**2)
        psigma = sigma
        sigma += (s)
        k += 1
    return sigma

s = calculation(1)
print(s)