#include <cmath>
#include <stdio.h>

double eval1(double *p)
{
    double x = p[0];
    double y = p[1];
    return 2 * x * (exp(x * x + y * y)) + 1;
}

double eval2(double *p)
{
    double x = p[0];
    double y = p[1];
    return 2 * y * (exp(x * x + y * y)) + 5;
}

double eval3(double *p)
{
    return p[0] + 2 * p[1] + 4 * sqrt(1 + pow(p[0], 2) + pow(p[1], 2));
}

void extremum_by_coordinate(double (*evallist[])(double *), double* xn)
{
    double speed = 0.1;
    double x[] = {0, 0};
    double d = 10;
    while (fabs(d) > pow(10, -6))
    {
        d = 0;
        for (int i = 0; i < 2; i++)
        {
            xn[i] = x[i] - speed * evallist[i](x);
            d += pow(xn[i], 2) - pow(x[i], 2);
            x[i] = xn[i];
        }
    }
}

double dihot(double *grad, double *xarr)
{
    int counter = 0;
    double x1 = -1;
    double x2 = 1;
    double xl, xr;
    double vx;
    double epsilon = pow(10, -6);
    bool f = 1;

    while (f)
    {
        xl = (x1 + x2) / 2 - epsilon / 100;
        xr = (x1 + x2) / 2 + epsilon / 100;
        double bl[] = {xarr[0] - xl * grad[0], xarr[1] - xl * grad[1]};
        double br[] = {xarr[0] - xr * grad[0], xarr[1] - xr * grad[1]};
        if (eval3(bl) > eval3(br))
        {
            x1 = xl;
        }
        else
        {
            x2 = xr;
        }
        counter++;
        vx = eval3(bl) - eval3(br);
        if (fabs(vx*100) < epsilon)
            f = 0;
    }
    return (x1 + x2) / 2;
}

void get_grad(double *p, double* grad)
{
    double pn = pow(10, -10);
    double p0[] = {p[0] + pn, p[1]};
    double p1[] = {p[0], p[1] + pn};
    grad[0] = (eval3(p0) - eval3(p)) / pn;
    grad[1] = (eval3(p1) - eval3(p)) / pn;
}

void quickest_decent(double *x)
{
    double speed = 0.1;
    x[0] = 0;
    x[1] = 0;
    double xn[] = {0, 0};
    double d = 1;
    while (fabs(d) > pow(10, -6))
    {
        double grad[2];
        get_grad(x, grad);
        speed = dihot(grad, x);
        d = 0;
        xn[0] = x[0] - speed * grad[0];
        d += pow(xn[0], 2) - pow(x[0], 2);
        x[0] = xn[0];
        xn[1] = x[1] - speed * grad[1];
        d += pow(xn[1], 2) - pow(x[1], 2);
        x[1] = xn[1];
    }
}

int main()
{
    double (*evallist[])(double *) = {eval1, eval2};
    double x1[2];
    extremum_by_coordinate(evallist, x1);
    printf("%lf %lf\n", x1[0], x1[1]);
    quickest_decent(x1);
    printf("%lf %lf\n", x1[0], x1[1]);
}