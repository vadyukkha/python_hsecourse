import os
import subprocess
import time

import matplotlib.pyplot as plt

# Пути к исполняемым файлам
executables = {
    "naive": "aio_multuthreading_multiprocessing/C_C++/executable_files/naive",
    "transposition": "aio_multuthreading_multiprocessing/C_C++/executable_files/transposition",
    "vectorization": "aio_multuthreading_multiprocessing/C_C++/executable_files/vectorization",
    "kernel": "aio_multuthreading_multiprocessing/C_C++/executable_files/kernel",
    "blocking": "aio_multuthreading_multiprocessing/C_C++/executable_files/blocking",
    "optimization": "aio_multuthreading_multiprocessing/C_C++/executable_files/optimization",
}


# Функция для компиляции исходников через make
def compile_code():
    print("[COMPILATION] >> Компиляция исходных файлов...")
    all_compiled = all(
        os.path.isfile(executable) for executable in executables.values()
    )
    if not all_compiled:
        try:
            subprocess.run(
                ["make"],
                cwd="aio_multuthreading_multiprocessing/C_C++/source",
                check=True,
            )  # Запуск make в нужной папке
            print("[COMPILATION] >> Компиляция завершена успешно.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при компиляции: {e}")
            exit(1)


# Функция для запуска теста
def run_test(executable, n):
    start_time = time.time()
    subprocess.run([executable, str(n)], check=True)
    return time.time() - start_time


if "__main__" == __name__:
    matrix_sizes = range(1, 1921)  # Диапазон размеров матриц

    results = {
        algo: [] for algo in executables
    }  # Результаты времени выполнения для каждого алгоритма

    compile_code()  # Сначала компилируем исходные файлы

    # Запуск тестов
    for algo, path in executables.items():
        print(f"[TEST] >> Тестируем {algo}... << [TEST]")
        for n in matrix_sizes:
            exec_time = run_test(path, n)
            GFLOPS = (2 * n**3) / (10**9 * exec_time)
            results[algo].append(GFLOPS)
            print(f"    [TEST] >> Размер матрицы {n}: {GFLOPS} GFLOPS")

    # np.save("aio_multuthreading_multiprocessing/C_C++/test_results.npy", results) # Сохранение результатов в файл

    plt.figure(figsize=(10, 6))  # Построение графиков

    for algo, times in results.items():
        plt.plot(matrix_sizes, times, label=algo)

    plt.xlabel("Matrix size (N x N)")
    plt.ylabel("GFLOPS")
    plt.title("Matrix multiplication performance")
    plt.legend()
    plt.grid(True)
    plt.savefig("aio_multuthreading_multiprocessing/C_C++/performance_plot.png")
    # plt.show()
