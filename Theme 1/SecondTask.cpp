#include <math.h>
#include <stdlib.h>
#include <stdio.h>

long double epsilon = pow(10, -6);
long double left = 0;
long double right = 1;

long double eval(long double x) {
    long double ans = (2.0/(1.0+x) - 3.0*sinl(x));
    return ans;
}

long double evaldydx(long double x) {
    long double ans = (-2/(pow(x,2)+2*x+1))-3*cos(x);
    return ans;
}

long double dihot() {
    int counter = 0;
    long double x1 = left;
    long double x2 = right;
    long double x = 0;
    long double vx;

    while (1) {
        x = (x1+x2) / 2;
        vx = eval(x);
        if (eval(x1) * vx > 0) {
            x1 = x;
        } else {
            x2 = x;
        }
        counter++;
        if (fabsl(vx) < epsilon) break;
    }
    printf("Метод дихотомии завершил работу за %d циклов.\n", counter);
    return x;
}

long double iteration() {
    long double x1 = left;
    long double x2 = right;
    long double dy = eval(x2)-eval(x1);
    dy = dy / fabsl(dy) * 0.3;

    long double x = x1;
    int counter = 0;

    while (fabsl(eval(x)) > epsilon) {
        x = x - dy * eval(x);
        counter++;
    }

    printf("Метод простой итерации завершил работу за %d циклов.\n", counter);
    return x;
}

long double newton() {
    long double x = left;
    int counter = 0;

    while (fabsl(eval(x)) > epsilon) {
        x = x - eval(x)/evaldydx(x);
        counter++;
    }
    printf("Метод Ньютона завершил работу за %d циклов.\n", counter);
    return x;
}

long double horde() {
    long double x = left;
    long double xprev = right;
    long double b;
    int counter = 0;

    while (fabsl(eval(x)) > epsilon) {
        b = x;
        x = x - eval(x)*((x-xprev)/(eval(x)-eval(xprev)));
        xprev = b;
        counter++;
    }
    printf("Метод секущих завершил работу за %d циклов.\n", counter);
    return x;
}

int main() {
    printf("%.16Lf\n", dihot());
    printf("%.16Lf\n", iteration());
    printf("%.16Lf\n", newton());
    printf("%.16Lf\n", horde());
    return 0;
}