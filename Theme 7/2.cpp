#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double eval1(double x, double y)
{
    return (pow(y, 2) + pow(x, 2) * y) / pow(x, 3);
}

double *Euler_First(double a, double b, double h, double y0, double (*eval)(double, double))
{
    int n = abs((b - a) / h);
    double *y = (double *)malloc(sizeof(double) * n + 1);
    double x = a;
    y[0] = y0;
    double buf;
    for (int i = 0; i < n; i++)
    {
        buf = y[i] + h / 2 * eval(x, y[i]);
        y[i + 1] = (y[i] + h * eval(x + h / 2, buf));
        x += h;
    }
    return y;
}

double prec_eval1(double x)
{
    return pow(x, 2) / (1 + x);
}

void print_answer(double a, double b, double h, double *arr, double (*eval)(double))
{
    double x = a;
    int n = abs((b - a) / h);
    for (int i = 0; i < n+1; i++)
    {
        printf("Вычисленный ответ в точке х = %lf: %lf Точный: %lf Разница: %lf\n", x, arr[i], eval(x), eval(x) - arr[i]);
        x += h;
    }
}

int main()
{
    double *arr = Euler_First(1, 2, 0.1, 0.5, eval1);
    print_answer(1, 2, 0.1, arr, prec_eval1);
    free(arr);
}