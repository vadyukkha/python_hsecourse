#pragma GCC target("avx2")
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <ctime>

#define min(a, b) ((a) < (b) ? (a) : (b))

// A vector of 256 / 32 = 8 floats (for AVX)
typedef float vec __attribute__ ((vector_size(32)));

// A helper function that allocates n vectors and initializes them with zeros
vec* alloc(int n) {
    vec* ptr = (vec*) std::aligned_alloc(32, 32 * n); // Allocate aligned memory
    memset(ptr, 0, 32 * n); // Initialize memory to zero
    return ptr;
}

// Update 6x16 submatrix C[x:x+6][y:y+16] using A[x:x+6][l:r] and B[l:r][y:y+16]
void kernel(const vec *a, const vec *b, vec *c, int x, int y, int l, int r, int n) {
    // Use 12 vector registers for manual accumulation (6x16 block)
    vec t00{}, t01{}, t10{}, t11{}, t20{}, t21{}, t30{}, t31{}, t40{}, t41{}, t50{}, t51{};

    for (int k = l; k < r; k++) {
        // Load one element of A and broadcast
        vec alpha0 = vec{} + a[(x + 0) * n + k];
        vec alpha1 = vec{} + a[(x + 1) * n + k];
        vec alpha2 = vec{} + a[(x + 2) * n + k];
        vec alpha3 = vec{} + a[(x + 3) * n + k];
        vec alpha4 = vec{} + a[(x + 4) * n + k];
        vec alpha5 = vec{} + a[(x + 5) * n + k];

        // Multiply B[k][y:y+16] by the broadcasted A values and accumulate
        t00 += alpha0 * b[(k * n + y) / 8 + 0];
        t01 += alpha0 * b[(k * n + y) / 8 + 1];
        t10 += alpha1 * b[(k * n + y) / 8 + 0];
        t11 += alpha1 * b[(k * n + y) / 8 + 1];
        t20 += alpha2 * b[(k * n + y) / 8 + 0];
        t21 += alpha2 * b[(k * n + y) / 8 + 1];
        t30 += alpha3 * b[(k * n + y) / 8 + 0];
        t31 += alpha3 * b[(k * n + y) / 8 + 1];
        t40 += alpha4 * b[(k * n + y) / 8 + 0];
        t41 += alpha4 * b[(k * n + y) / 8 + 1];
        t50 += alpha5 * b[(k * n + y) / 8 + 0];
        t51 += alpha5 * b[(k * n + y) / 8 + 1];
    }

    // Write the results back to C
    c[((x + 0) * n + y) / 8 + 0] += t00;
    c[((x + 0) * n + y) / 8 + 1] += t01;
    c[((x + 1) * n + y) / 8 + 0] += t10;
    c[((x + 1) * n + y) / 8 + 1] += t11;
    c[((x + 2) * n + y) / 8 + 0] += t20;
    c[((x + 2) * n + y) / 8 + 1] += t21;
    c[((x + 3) * n + y) / 8 + 0] += t30;
    c[((x + 3) * n + y) / 8 + 1] += t31;
    c[((x + 4) * n + y) / 8 + 0] += t40;
    c[((x + 4) * n + y) / 8 + 1] += t41;
    c[((x + 5) * n + y) / 8 + 0] += t50;
    c[((x + 5) * n + y) / 8 + 1] += t51;
}

// Matrix multiplication using aligned memory
void matmul(const float *_a, const float *_b, float *_c, int n) {
    if (n == 1) _c[0] = _a[0] * _b[0];
    int nx = (n + 5) / 6 * 6; // Round up to a multiple of 6
    int ny = (n + 15) / 16 * 16; // Round up to a multiple of 16

    // Allocate aligned vectors
    vec *a = alloc(nx * ny);
    vec *b = alloc(nx * ny);
    vec *c = alloc(nx * ny);

    // Copy the input matrices into the aligned vectors
    for (int i = 0; i < n; i++) {
        memcpy(&a[i * ny], &_a[i * n], 4 * n);
        memcpy(&b[i * ny], &_b[i * n], 4 * n); // No need to transpose B
    }

    const int s3 = 64;  // Number of columns in B
    const int s2 = 120; // Number of rows in A
    const int s1 = 240; // Number of rows in B

    // Blocked matrix multiplication
    for (int i3 = 0; i3 < ny; i3 += s3) {
        for (int i2 = 0; i2 < nx; i2 += s2) {
            for (int i1 = 0; i1 < ny; i1 += s1) {
                for (int x = i2; x < min(i2 + s2, nx); x += 6) {
                    for (int y = i3; y < min(i3 + s3, ny); y += 16) {
                        kernel(a, b, c, x, y, i1, min(n, i1 + s1), ny);
                    }
                }
            }
        }
    }

    // Copy the result back into _c
    for (int i = 0; i < n; i++) {
        memcpy(&_c[i * n], &c[i * ny], 4 * n);
    }

    // Free the allocated aligned memory
    std::free(a);
    std::free(b);
    std::free(c);
}

// Initialize a matrix with random values
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
    float* c = new float[n * n](); // Initialize C with zeros

    init_matrix(a, n);
    init_matrix(b, n);

    matmul(a, b, c, n);

    double time_spent = (double)(clock() - start) / CLOCKS_PER_SEC;
    // std::cout << "Runtime is " << time_spent << " seconds." << std::endl;

    delete[] a;
    delete[] b;
    delete[] c;

    return 0;
}
