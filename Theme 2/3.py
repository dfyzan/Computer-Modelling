import math

def hyperbola_input():
    a, b, c, d, e, f  = map(float, input("Введите шесть коэффициентов уравнения Axx, Axy, Ayy, Bx, By, и C: ").split())
    return [a, b, c, d, e, f]

def point_input():
    x, y = map(float, input("Введите две координаты точки: ").split())
    return [x, y]

def is_point_on_hyperbola(p, h):
    return (h[0] * p[0]**2 + h[1] * p[0] * p[1] + h[2] * p[1] ** 2 + h[3] * p[0] + h[4] * p[1] + h[5]) == 0

def hyperbola_to_canonical(h):
    A, B, C, D, E, F = h
    angle = 0
    x0 = 0
    y0 = 0
    swapped = False
    xm = False
    ym = False
    if (D != 0 or E != 0):
        if (B == 0):
            y0 = (-E) / (2 * C)
            x0 = (-D) / (2 * A)
        else:
            y0 = (-1*D * B + 2 * A * E) / (B**2 - 4 * A * C)
            x0 = (-2 * C * y0 - E) / B
    M = F + A * x0**2 + B * x0 * y0 + C * y0**2 + D * x0 + E * y0
    if (B == 0):
        a = (-1 * M) / A
        b = (M) / C
    else:
        angle = (1/2) * math.asin(B / (math.sqrt(C**2 - 2 * A * C + A**2 + B**2)))
        a = -1 * M / (A * math.cos(angle)**2 + C * math.sin(angle)**2 + B * math.sin(angle) * math.cos(angle))
        b = M / (A * math.sin(angle)**2 + C * math.cos(angle)**2 - B * math.sin(angle) * math.cos(angle))
        if (a < 0 and b > 0):
            angle += math.pi/2

    if (A-C != 0):
        angle = 1/2 * math.atan(B/(A-C))
    else:
        angle = 1/2 * math.acos(0)
    

    l1, l2 = -(-(A+C)-math.sqrt((A+C)**2-4*(A*C-(1/2*B)**2)))/(2), -(-(A+C)+math.sqrt((A+C)**2-4*(A*C-(1/2*B)**2)))/(2)
    i1, i2 = (A*C*F+D*E*(1/8)*B*2) - (((1/4)*D**2)*C+((1/4)*E**2)*A+((1/4)*B**2)*F), A*C - ((1/4)*B**2)

    if (i1 != 0):
        if (l1*i1 < 0):
            l1, l2 = l2, l1
        a = -(i1/(l1*i2))
        b = (i1/(l2*i2))
    else:
        if (l1 < 0):
            l1, l2 = l2, l1
        a = 1/l1
        b = 1/l2

    if (a < 0 and b < 0):
        swapped = True
        a, b = b, a
        a = a * -1
        b = b * -1
    elif (a < 0):
        xm = True
        a = a * -1
    elif (b < 0):
        ym = True
        b = b * -1

    a = math.sqrt(abs(a))
    b = math.sqrt(abs(b))

    return [a, b, x0, y0, angle, swapped, xm, ym]

def hyperbola_foci(a, b, x0, y0, angle, swapped, xm, ym):
    c = math.sqrt(a**2 + b**2)
    swapped = False
   
    p1 = [-c, 0]
    if (swapped):
        p1 = [0, -c]
    
    
    b = p1[0]
    p1[0] = p1[0] * math.cos(angle) - p1[1] * math.sin(angle)
    p1[1] = b * math.sin(angle) + p1[1] * math.cos(angle)
    p1[0] = p1[0] + x0
    p1[1] = p1[1] + y0

    
    p2 = [c, 0]
    if (swapped):
        p2 = [0, c]

    b = p2[0]
    p2[0] = p2[0] * math.cos(angle) - p2[1] * math.sin(angle)
    p2[1] = b * math.sin(angle) + p2[1] * math.cos(angle)
    p2[0] = p2[0] + x0
    p2[1] = p2[1] + y0
    
    if (ym):
        p2[1], p1[1] = p1[1], p2[1]
    if (xm):
        p2[0], p1[0] = p1[0], p2[0]
    return [p1, p2]

h = hyperbola_input()
#p = point_input()
#if (is_point_on_hyperbola(p, h)):
#    print("Точка принадлежит гиперболе")
#else:
#    print("Точка не принадлежит гиперболе")
a, b, x0, y0, angle, swapped, xm, ym = hyperbola_to_canonical(h)
p1, p2 = hyperbola_foci(a, b, x0, y0, angle, swapped, xm, ym)
print(f"Фокусы гиперболы: ({p1[0]};{p1[1]}) и ({p2[0]};{p2[1]})")

c = math.sqrt(a**2 + b**2)
print(f"Длина действительной и мнимой полуоси гиперболы: ({a}) и ({b})")
e = c/a
print(f"Эксцентриситет гиперболы: ({e})")
d = abs(2*a/e)
print(f"Расстояние между директрисами гиперболы: ({d})")