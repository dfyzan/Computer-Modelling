x1, y1 = map(float, input("Введите вещественный и мнимый коэффициент первого комплексного числа: ").split())
x2, y2 = map(float, input("Введите вещественный и мнимый коэффициент второго комплексного числа: ").split())
x3, y3 = map(float, input("Введите вещественный и мнимый коэффициент второго комплексного числа: ").split())

z1 = complex(x1, y1)
z2 = complex(x2, y2)
z3 = complex(x3, y3)

print("Сумма первых двух комплексных чисел равна ", z1 + z2)
print("Разность первых двух комплексных чисел равна ", z1 - z2)
print("Произведение первых двух комплексных чисел равно ", z1 * z2)
print("Частное первых двух комплексных чисел равно ", z1 / z2)

print("Четвёртая степень третьего комплексного числа равна ", pow(z3, 4))
print("Корень третьей степени третьего комплексного числа равен ", pow(z3, 1.0/3.0))
