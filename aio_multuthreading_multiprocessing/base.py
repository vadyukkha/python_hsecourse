import time


def foo1(x: int) -> None:
    print(x**2)
    time.sleep(3)
    print("Foo1 done.")


def foo2(x: int) -> None:
    print(x**0.5)
    time.sleep(3)
    print("Foo2 done.")


def main() -> None:
    foo1(4)
    foo2(4)


if "__main__" == __name__:
    start_time = time.time()

    main()

    execution_time = time.time() - start_time
    print(f"Время выполнения: {execution_time} секунд")
