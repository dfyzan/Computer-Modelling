#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double eval1(double x, double y)
{
    return (-1 * y * tan(x) + sin(x * 2));
}

double *Euler_Cauchy(double a, double b, double h, double y0, double (*eval)(double, double))
{
    int n = abs((b - a) / h);
    double *y = (double *)malloc(sizeof(double) * n + 1);
    double x = a;
    y[0] = y0;
    for (int i = 0; i < n; i++)
    {
        y[i+1] = (y[i] + h * eval(x, y[i]));
        x += h;
    }
    return y;
}

double prec_eval1(double x)
{
    return -2 * pow(cos(x), 2) + cos(x);
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
    double *arr = Euler_Cauchy(0, 1, 0.1, -1, eval1);
    print_answer(0, 1, 0.1, arr, prec_eval1);
    free(arr);
}