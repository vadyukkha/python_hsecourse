import asyncio
import time


async def foo1(x: int) -> None:
    print(x**2)
    await asyncio.sleep(3)
    print("Foo1 done.")


async def foo2(x: int) -> None:
    print(x**0.5)
    await asyncio.sleep(3)
    print("Foo2 done.")


async def main() -> None:
    task1 = asyncio.create_task(foo1(4))
    task2 = asyncio.create_task(foo2(4))

    await task1
    await task2


if "__main__" == __name__:
    start_time = time.time()

    asyncio.run(main())

    execution_time = time.time() - start_time
    print(f"Время выполнения: {execution_time} секунд")
