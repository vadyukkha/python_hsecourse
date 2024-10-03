#include <iostream>
#include <cstdlib>
#include <cstring>
#include <ctime> 

// a vector of 256 / 32 = 8 floats
typedef float vec __attribute__ (( vector_size(32) ));

// a helper function that allocates n vectors and initializes them with zeros
vec* alloc(int n) {
    vec* ptr = (vec*) std::aligned_alloc(32, 32 * n);
    memset(ptr, 0, 32 * n);
    return ptr;
}

void matmul(const float *_a, const float *_b, float * __restrict__ c, int n) {
    int nB = (n + 7) / 8; // number of 8-element vectors in a row (rounded up)

    vec *a = alloc(n * nB);
    vec *b = alloc(n * nB);

    // move both matrices to the aligned region
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            a[i * nB + j / 8][j % 8] = _a[i * n + j];
            b[i * nB + j / 8][j % 8] = _b[j * n + i]; // <- b is still transposed
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            vec s{}; // initialize the accumulator with zeros

            // vertical summation
            for (int k = 0; k < nB; k++)
                s += a[i * nB + k] * b[j * nB + k];
            
            // horizontal summation
            for (int k = 0; k < 8; k++)
                c[i * n + j] += s[k];
        }
    }

    std::free(a);
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
