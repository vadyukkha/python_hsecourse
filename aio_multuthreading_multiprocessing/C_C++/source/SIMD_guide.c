#pragma GCC target("avx512")
#include <time.h>
#include <stdio.h>

const int n = 1e5;
int a[n], s = 0;

int main() {
    clock_t start = clock();

    for (int t = 0; t < 100000; t++)
        for (int i = 0; i < n; i++)
            s += a[i];

    double time_spent = (double)(clock() - start) / CLOCKS_PER_SEC;
    printf("Runtime is %lf\n", time_spent);
    return 0;
}
