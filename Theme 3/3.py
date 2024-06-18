def calculation():
    s1 = 9
    s2 = 1/2
    sigma = 0
    psigma = -1
    while(abs(sigma-psigma) > 10 ** (-6)):
        s1 /= 2
        s2 /= -3
        psigma = sigma
        sigma += (s1 + s2)
    return sigma

s = calculation()
print(s)