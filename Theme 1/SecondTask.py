import math

epsilon = 10**(-6)
left = 0
right = 1


def eval(x):
    ans = (2/(1+x) - 3*math.sin(x))
    return ans

def evaldydx(x):
    ans = (-2/(x**2+2*x+1))-3*math.cos(x)
    return ans

def dihot():
    counter = 0
    x1 = left
    x2 = right
    x = 0

    while (True):
        x = (x1+x2)/2
        vx = eval(x)
        if (eval(x1) * vx > 0):
            x1 = x
        else:
            x2 = x
        counter += 1
        if (abs(vx) < epsilon): break
    print("Метод дихотомии завершил работу за ", counter, " циклов.")
    return(x)

def iteration():
    x1 = left
    x2 = right
    dy = eval(x2)-eval(x1)
    dy = dy / abs(dy) * 0.3 # От значения множителя зависит скорость сходимости метода.
    
    x = x1
    counter = 0

    while(abs(eval(x)) > epsilon):
        x = x - dy*eval(x)
        counter += 1

    print("Метод простой итерации завершил работу за ", counter, " циклов.")
    return(x)

def newton():
    x1 = left
    x2 = right
    
    x = x1
    counter = 0

    while(abs(eval(x)) > epsilon):
        x = x - eval(x)/evaldydx(x)
        counter += 1

    print("Метод Ньютона завершил работу за ", counter, " циклов.")
    return(x)

def horde():
    x1 = left
    x2 = right

    x = x1
    xprev = x2
    counter = 0

    while(abs(eval(x)) > epsilon):
        b = x
        x = x - eval(x)*((x-xprev)/(eval(x)-eval(xprev)))
        xprev = b
        counter += 1

    print("Метод секущих завершил работу за ", counter, " циклов.")
    return(x)



print(dihot())
print(iteration())
print(newton())
print(horde())