import multiprocessing as mp
import time

import numpy as np


class MatrixMultiprocessing:
    def __init__(self) -> None:
        pass

    def matrix_multiply_worker(self, A, B, output, idx):
        result_slice = np.dot(A, B)
        output[idx] = result_slice

    def parallel_matrix_multiply(self, A, B, num_processes=4):
        # Determine capacity of result matrix
        result = np.zeros((A.shape[0], B.shape[1]))

        # Divide matrix A for each process
        chunk_size = A.shape[0] // num_processes
        processes = []
        output = mp.Manager().dict()

        for i in range(num_processes):
            start_row = i * chunk_size
            end_row = (i + 1) * chunk_size if i != num_processes - 1 else A.shape[0]
            A_slice = A[start_row:end_row]

            # Create and begin new process
            p = mp.Process(
                target=self.matrix_multiply_worker, args=(A_slice, B, output, i)
            )
            processes.append(p)
            p.start()

        # Ожидаем завершения всех процессов
        for p in processes:
            p.join()

        # Merge results from all processes
        result = np.vstack([output[i] for i in range(num_processes)])

        return result


class MatrixNumpy:
    def __init__(self) -> None:
        pass

    def matrixMultiply(self, A, B):
        return np.dot(A, B)


def whatTimeNeeded(func, A, B):
    start_time = time.time()
    func(A, B)
    return time.time() - start_time


if __name__ == "__main__":
    # Testing data
    A = np.random.rand(10_000, 10_000)
    B = np.random.rand(10_000, 10_000)

    matrix_numpy = MatrixNumpy()
    matrix_multiprocessing = MatrixMultiprocessing()

    # Compare time with NumPy
    execution_time_numpy = whatTimeNeeded(matrix_numpy.matrixMultiply, A, B)
    print(f"Время выполнения с NumPy: {execution_time_numpy} секунд")

    # Compare time with multiprocessing
    execution_time_mp = whatTimeNeeded(
        matrix_multiprocessing.parallel_matrix_multiply, A, B
    )
    print(f"Время выполнения с multiprocessing: {execution_time_mp} секунд")
