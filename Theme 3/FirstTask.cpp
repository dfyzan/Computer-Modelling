#include <complex.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

double a = 1;
double b = 2;

double eval(double x) {
    double res = pow(x, 4) * (1/(9+pow(x, 2)));
    return res;
}

double rectangle() {
    double sigma, psigma, h, x;
    for (int i = 1; i < 9; i++) {
        int N = pow(10, i);
        psigma = sigma;
        sigma = 0;
        h = (b-a) / N;
        x = a;
        for (int j = 1; j < N; j++) {
            sigma += eval((x+x+h) / 2);
            x += h;
        }
        sigma *= h;
        if (fabs(sigma - psigma) < pow(10, -6)) i = 9;
    }
    return sigma;
}

int main () {
    
    return 0;
}