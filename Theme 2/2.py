import math


def vector_input():
    x, y, z = map(float, input("Введите три координаты вектора: ").split())
    v = [x, y, z]
    return v


def length(v):
    l = (v[0] ** 2 + v[1] ** 2 + v[2] ** 2) ** (0.5)
    return l


def sum(v1, v2):
    v = [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]
    return v


def dif(v1, v2):
    v = [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]
    return v


def ang(v1, v2):
    scal_mult = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
    if length(v1) == 0 or length(v2) == 0:
        return 0
    cos = scal_mult / (length(v1) * length(v2))
    angle = math.acos(cos)
    return angle


def par(v1, v2):
    vect_mult = [v1[1]*v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0]*v2[1] - v1[1] * v2[0]]
    return (length(vect_mult) == 0)
    
def are_one_plane(v1, v2, v3):
    vect_mult = [v1[1]*v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0]*v2[1] - v1[1] * v2[0]]
    scal_mult = v3[0] * vect_mult[0] + v3[1] * vect_mult[1] + v3[2] * vect_mult[2]
    return (scal_mult == 0)

v1 = vector_input()
v2 = vector_input()
v3 = vector_input()


print(f"\nДлины векторов 1, 2 и 3 равны: {length(v1)} {length(v2)} {length(v3)}")
print(
    f"\nУгол между векторами 1 и 2 равен: {ang(v1, v2)} радиан или {math.degrees(ang(v1, v2))} градусов."
)
print(
    f"Угол между векторами 1 и 3 равен: {ang(v1, v3)} радиан или {math.degrees(ang(v1, v3))} градусов."
)
print(
    f"Угол между векторами 2 и 3 равен: {ang(v2, v3)} радиан или {math.degrees(ang(v2, v3))} градусов."
)

print(f"\nСумма векторов 1 и 2 равна: {sum(v1, v2)}")
print(f"Сумма векторов 1 и 3 равна: {sum(v1, v3)}")
print(f"Сумма векторов 2 и 3 равна: {sum(v2, v3)}")

print(f"\nРазность векторов 1 и 2 равна: {dif(v1, v2)}")
print(f"Разность векторов 1 и 3 равна: {dif(v1, v3)}")
print(f"Разность векторов 2 и 3 равна: {dif(v2, v3)}\n")

if par(v1, v2):
    print("Вектора 1 и 2 парралельны.")
if par(v1, v3):
    print("Вектора 1 и 3 парралельны.")
if par(v3, v2):
    print("Вектора 2 и 3 парралельны.")

if are_one_plane(v1, v2, v3):
    print("Вектора лежат в одной плоскости.")
