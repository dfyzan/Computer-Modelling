#include <complex.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main () {
    double a, b;
    
    char c;
    printf("Введите первое комплексное число в виде a +/- bi\n");
    scanf ("%lf %c %lfi", &a, &c, &b);
    if (c == '-') b*=-1;
    complex <double> z1(a,b);
    printf("Введите второе комплексное число в виде a +/- bi\n");
    scanf ("%lf %c %lfi", &a, &c, &b);
    if (c == '-') b*=-1;
    complex <double> z2(a,b);
    printf("Введите третье комплексное число в виде a +/- bi\n");
    scanf ("%lf %c %lfi", &a, &c, &b);
    if (c == '-') b*=-1;
    complex <double> z3(a,b);

    complex <double> sum;
    sum = z1 + z2;
    printf("Сумма первых двух комплексных чисел равна %lf + %lfi\n", real(sum), imag(sum));

    complex <double> dif;
    dif = z1 - z2;
    printf("Разность первых двух комплексных чисел равна %lf + %lfi\n", real(dif), imag(dif));

    complex <double> mul;
    mul = z1 * z2;
    printf("Произведение первых двух комплексных чисел равно %lf + %lfi\n", real(mul), imag(mul));

    complex <double> div;
    div = z1 / z2;
    printf("Частное первых двух комплексных чисел равно %lf + %lfi\n", real(div), imag(div));

    complex <double> power;
    power = pow(z3, 4);
    printf("Четвёртая степень третьего комплексного числа равна %lf + %lfi\n", real(power), imag(power));

    complex <double> root;
    root = pow(z3, 1.0/3.0);
    printf("Корень третьей степени третьего комплексного числа равен %lf + %lfi\n", real(root), imag(root));

    return 0;
}