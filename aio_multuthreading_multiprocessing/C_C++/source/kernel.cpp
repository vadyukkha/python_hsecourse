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

// update 6x16 submatrix C[x:x+6][y:y+16]
// using A[x:x+6][l:r] and B[l:r][y:y+16]
void kernel(vec *a, vec *b, vec *c, int x, int y, int l, int r, int n) {
    vec t[6][2]{}; // will be zero-filled and stored in ymm registers

    for (int k = l; k < r; k++) {
        for (int i = 0; i < 6; i++) {
            // broadcast a[x + i][k] into a register
            vec alpha = vec{} + a[(x + i) * n + k]; // converts to a broadcast
            // multiply b[k][y:y+16] by it and update t[i][0] and t[i][1]
            for (int j = 0; j < 2; j++)
                t[i][j] += alpha * b[(k * n + y) / 8 + j]; // converts to an fma
        }
    }

    // write the results back to C
    for (int i = 0; i < 6; i++)
        for (int j = 0; j < 2; j++)
            c[((x + i) * n + y) / 8 + j] += t[i][j];
}

void matmul(const float *_a, const float *_b, float *_c, int n) {
    // to simplify the implementation, we pad the height and width
    // so that they are divisible by 6 and 16 respectively
    int nx = (n + 5) / 6 * 6;
    int ny = (n + 15) / 16 * 16;
    
    vec *a = alloc(nx * ny);
    vec *b = alloc(nx * ny);
    vec *c = alloc(nx * ny);

    for (int i = 0; i < n; i++) {
        memcpy(&a[i * ny], &_a[i * n], 4 * n);
        memcpy(&b[i * ny], &_b[i * n], 4 * n); // we don't need to transpose b this time
    }

    for (int x = 0; x < nx; x += 6)
        for (int y = 0; y < ny; y += 16)
            kernel(a, b, c, x, y, 0, n, ny);

    for (int i = 0; i < n; i++)
        memcpy(&_c[i * n], &c[i * ny], 4 * n);
    
    std::free(a);
    std::free(b);
    std::free(c);
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
