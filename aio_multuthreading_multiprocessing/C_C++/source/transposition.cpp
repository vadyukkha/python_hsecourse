#include <iostream>
#include <cstdlib>
#include <cstring>
#include <ctime> 

void matmul(const float *a, const float *_b, float *c, int n) {
    float *b = new float[n * n];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            b[i * n + j] = _b[j * n + i];
    
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++)
                c[i * n + j] += a[i * n + k] * b[j * n + k]; // <- note the indices

    std::free(b);
}

void init_matrix(float* mat, int n) {
    for (int i = 0; i < n * n; i++) {
        mat[i] = static_cast<float>(std::rand()) / RAND_MAX;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Использование: " << argv[0] << " <размер_матрицы>" << std::endl;
        return 1; // Ошибка, если недостаточно аргументов
    }
    clock_t start = clock();
    int n = std::atoi(argv[1]);
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    float* a = new float[n * n];
    float* b = new float[n * n];
    float* c = new float[n * n]();

    init_matrix(a, n);
    init_matrix(b, n);

    matmul(a, b, c, n);

    double time_spent = (double)(clock() - start) / CLOCKS_PER_SEC;
    // std::cout << "Runtime is " << time_spent << std::endl;
    delete[] a;
    delete[] b;
    delete[] c;

    return 0;
}
