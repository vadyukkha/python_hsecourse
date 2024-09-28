from typing import Callable

# ---------------- Example 1 ------------------------


def demo_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        print("Welcome to decorator.")
        func(*args, **kwargs)
        print("Bye bye!")

    return wrapper


@demo_decorator
def hello_func(name: str) -> None:
    print(f"Hello, {name}!")


# Testing
hello_func("Vadik")

print()
# ---------------- Example 2 ------------------------


def operation_decorator(operation: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(a: int, b: int) -> int:
            print(f"You selected the {operation} operation")

            if operation == "add":
                res = func(a, b)
            elif operation == "subtract":
                res = a - b
            elif operation == "multiply":
                res = a * b
            elif operation == "divide":
                if b != 0:
                    res = a / b
                else:
                    raise ValueError("Division by zero is not allowed.")
            else:
                raise ValueError("Unknown operation.")

            print(f"The decorator done {operation} operation successfully!")
            return res

        return wrapper

    return decorator


@operation_decorator("add")
def sum_func(a: int, b: int) -> int:
    return a + b


print(sum_func(10, 5))  # Для суммы


@operation_decorator("subtract")
def sum_func(a: int, b: int) -> int:
    return a + b


print(sum_func(10, 5))  # Для вычетания


@operation_decorator("multiply")
def sum_func(a: int, b: int) -> int:
    return a + b


print(sum_func(10, 5))  # Для умножения


@operation_decorator("divide")
def sum_func(a: int, b: int) -> int:
    return a + b


print(sum_func(10, 5))  # Для деления

print()
# ---------------- Example 3 ------------------------


def logging_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(
            f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}"
        )

        result = func(*args, **kwargs)

        print(f"Function '{func.__name__}' returned: {result}")

        return result

    return wrapper


@logging_decorator
def multiply(a: int, b: int) -> int:
    return a * b


@logging_decorator
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


# Testing
result1 = multiply(3, 4)
result2 = greet("Vadik", greeting="You're welcome")
