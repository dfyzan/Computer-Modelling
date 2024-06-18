import math


def eval1(x, y):
    return -1 * y * math.tan(x) + math.sin(x * 2)


def Euler_Cauchy(a, b, h, y0, eval):
    y = [y0]
    n = int(abs(b - a) / h)
    x = a
    for i in range(n):
        y.append(y[i] + h * eval(x, y[i]))
        x += h
    return y


def prec_eval1(x):
    return -2 * math.cos(x) ** 2 + math.cos(x)


def print_answer(a, h, arr, eval):
    x = a
    for i in arr:
        print(f"Вычисленный ответ в точке х = {x:.1f}: {i} Точный: {eval(x)} Разница: {eval(x)-i}")
        x += h


arr = Euler_Cauchy(0, 1, 0.1, -1, eval1)
print_answer(0, 0.1, arr, prec_eval1)
