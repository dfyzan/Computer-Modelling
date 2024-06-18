def eval1(x, y):
    return (y**2 + y * x**2) / x**3


def Euler_First(a, b, h, y0, eval):
    y = [y0]
    n = int(abs(b - a) / h)
    x = a
    for i in range(n):
        b = y[i]+h/2*eval(x, y[i])
        y.append(y[i] + h * eval(x+h/2, b))
        x += h
    return y


def prec_eval1(x):
    return x**2 / (1 + x)


def print_answer(a, h, arr, eval):
    x = a
    for i in arr:
        print(
            f"Вычисленный ответ в точке х = {x:.1f}: {i} Точный: {eval(x)} Разница: {eval(x)-i}"
        )
        x += h


arr = Euler_First(1, 2, 0.1, 0.5, eval1)
print_answer(1, 0.1, arr, prec_eval1)
