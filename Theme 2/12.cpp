#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

class vector
{
private:
    int dim;
    double *v;
    int number;
    friend vector operator-(vector &v1, vector &v2);
    friend vector operator*(double k, vector &v);
    friend class matrix;

public:
    static int count;
    vector();
    vector(int dim);
    vector(int d, double *vec);
    vector(vector &vect);
    ~vector();
    vector &operator=(const vector &vect);
    vector operator+(const vector &vect);
    vector operator*(double k);
    double operator*(const vector &vect);
    vector operator-();
    vector operator^(int k);

    double length();
    bool operator<(const vector &vect);
    friend bool are_parralel(vector v1, vector v2);
    friend vector vect_mult(vector v1, vector v2);

    void print();

    int operator[](int i);
};

int vector::count = 0;

vector::vector()
{
    number = count;
    count++;
    dim = 0;
    v = new double[dim];
}

vector::vector(int d)
{
    number = count;
    count++;
    dim = d;
    v = new double[dim];
    for (int i = 0; i < dim; i++)
        v[i] = 0;
}

vector::vector(int d, double *vec)
{
    number = count;
    count++;
    dim = d;
    v = new double[dim];
    for (int i = 0; i < dim; i++)
        v[i] = vec[i];
}

vector::vector(vector &vect)
{
    number = count;
    count++;
    dim = vect.dim;
    v = new double[dim];
    for (int i = 0; i < dim; i++)
        v[i] = vect[i];
}

vector::~vector()
{
    delete[] v;
}

vector operator-(vector &v1, vector &v2)
{
    vector res(v1.dim);
    for (int i = 0; i < v1.dim; i++)
        res.v[i] = v1.v[i] - v2.v[i];
    return res;
}

vector operator*(double k, vector &v)
{
    vector res(v.dim);
    for (int i = 0; i < v.dim; i++)
        res.v[i] = v.v[i] * k;
    return res;
}

vector &vector::operator=(const vector &vect)
{
    for (int i = 0; i < dim; i++)
        v[i] = vect.v[i];
    return *this;
}

vector vector::operator+(const vector &vect)
{
    vector res(dim);
    for (int i = 0; i < dim; i++)
        res.v[i] = v[i] + vect.v[i];
    return res;
}

vector vector::operator*(double k)
{
    vector res(dim);
    for (int i = 0; i < dim; i++)
        res.v[i] = v[i] * k;
    return res;
}

double vector::operator*(const vector &vect)
{
    int sum = 0;
    for (int i = 0; i < dim; i++)
        sum += v[i] * vect.v[i];
    return sum;
}

vector vector::operator-()
{
    vector res(dim);
    for (int i = 0; i < dim; i++)
        res.v[i] = v[i] * (-1);
    return res;
}

vector vector::operator^(int k)
{
    vector res(dim);
    for (int i = 0; i < dim; i++)
    {
        res.v[i] = pow(v[i], k);
    }
    return res;
}

void vector::print()
{
    for (int i = 0; i < dim; i++)
        printf("%lf,", v[i]);
    printf(")\n");
}

int vector::operator[](int i)
{
    return v[i];
}

bool vector::operator<(const vector &vect)
{
    bool f = true;
    for (int i = 0; i < dim; i++)
        if (v[i] > vect.v[i])
            f = false;
    return f;
}

double vector::length() {
    double sum = 0;
    for(int i = 0; i < dim; i++) {
        sum += pow(v[i], 2);
    }
    return (sqrt(sum));
}

double angle(vector v1, vector v2) {
    double scal_mult = v1 * v2;
    double l1 = v1.length();
    double l2 = v2.length();
    if (l2 == 0 || l2 == 0) return 0;
    double cos = scal_mult / (l1 * l2);
    double angle = acos(cos);
    return angle;
}

bool are_parralel(vector v1, vector v2) {
    if (v1.dim == 2) return (v1[0]*v2[1] - v1[1] * v2[0] == 0);
    vector vm = vect_mult(v1, v2);
    return (vm.length() == 0);
}

bool are_one_plane(vector v1, vector v2, vector v3) {
    vector m1 = vect_mult(v1, v2);
    vector m2 = m1 * v3;
    return (m2.length() == 0);
}

vector vect_mult(vector v1, vector v2) {
    double arr[3] = {v1[1]*v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0]*v2[1] - v1[1] * v2[0]};
    vector ans(3, arr);
    return ans;
}

int main()
{
    double arr1[2] = {1, 2};
    double arr2[2] = {-11, -22};
    double arr3[2] = {2, 3};
    vector v1(2, arr1);
    vector v2(2, arr2);
    vector v3(2, arr3);

    printf("Сумма векторов 1 и 2: ");
    vector s1 = v1 + v2;
    s1.print();
    printf("Сумма векторов 1 и 3: ");
    s1 = v1 + v3;
    s1.print();
    printf("Сумма векторов 2 и 3: ");
    s1 = v3 + v2;
    s1.print();

    printf("Разность векторов 1 и 2: ");
    s1 = v1 - v2;
    s1.print();
    printf("Разность векторов 1 и 3: ");
    s1 = v1 - v3;
    s1.print();
    printf("Разность векторов 2 и 3: ");
    s1 = v2 - v3;
    s1.print();

    printf("Длины векторов 1, 2 и 3 равны: %lf, %lf, %lf\n", v1.length(), v2.length(), v3.length());

    printf("Угол между векторами 1 и 2 равен: %lf\n", angle(v1, v2));
    printf("Угол между векторами 1 и 3 равен: %lf\n", angle(v1, v3));
    printf("Угол между векторами 2 и 3 равен: %lf\n", angle(v2, v3));
    if (are_parralel(v1, v2) || are_parralel(v1, v3) || are_parralel(v2, v3)) printf("Некоторые вектора параллельны.");
}
