# Python Decorators Tutorial

Декораторы в Python — это особый тип функций, предназначенный для изменения поведения других функций или методов. Они позволяют "оборачивать" одну функцию другой функцией, тем самым добавляя к ней дополнительную функциональность без изменения её исходного кода.

## 1. Что такое декоратор?
Декоратор — это функция, которая принимает другую функцию (или метод) как аргумент и возвращает новую функцию. Этот механизм позволяет легко добавлять к существующим функциям новые возможности, такие как логирование, управление доступом, кеширование и т.д.

Проще говоря, декоратор «оборачивает» исходную функцию и делает с ней что-то дополнительное до или после её вызова.

## 2. Для чего используются декораторы?
Декораторы используются для:

- Повторного использования кода: Часто используемая функциональность (например, логирование или проверка прав доступа) может быть вынесена в декораторы и применяться к разным функциям.
- Управления побочными эффектами: Декораторы могут контролировать и изменять выполнение функции без изменения её исходного кода.
- Облегчения кода: Они помогают сделать код более читабельным и структурированным.

## 3. Примеры использования

### Example 1: Простой декоратор

В первом примере `demo_decorator` используется для изменения поведения функции `hello_func`. Декоратор печатает приветственное сообщение перед вызовом функции и прощальное сообщение после ее завершения.


```python
from typing import Callable

def demo_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        print("Welcome to decorator.")
        func(*args, **kwargs)
        print("Bye bye!")
    return wrapper

@demo_decorator
def hello_func(name: str) -> None:
    print(f"Hello, {name}!")
```

**How it works:**
- `@demo_decorator` применяется к `hello_func`, поэтому каждый раз, когда вызывается `hello_func`, декоратор будет выполнять код до и после функции.
- Запуск `hello_func(«Vadik»)` выведет:

    ```
    Welcome to decorator.
    Hello, Vadik!
    Bye bye!
    ```

### Example 2: Декоратор с использованием параметров для операций

В этом примере декоратор `operation_decorator` принимает строковый аргумент, задающий операцию (сложение, вычитание, умножение, деление). Основываясь на выбранной операции, декоратор изменяет поведение `sum_func`, которая изначально складывает только два числа.

```python
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
```

**How it works:**
- Декоратор принимает аргумент (`operation`), который определяет, какую математическую операцию нужно выполнить.
- Исходя из типа операции, он изменяет поведение `sum_func`.
- Запустим следующий код:
  
  ```python
  print(sum_func(10, 5))  # For add, subtract, multiply, and divide operations
  ```

  Вывод будет отличаться в зависимости от того, какая операция была выбрана при применении декоратора.


### Example 3: Декоратор логирования

Этот пример демонстрирует декоратор логирования, который записывает в журнал имя функции, ее аргументы и возвращаемое значение.

```python
def logging_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Function '{func.__name__}' returned: {result}")
        
        return result
    return wrapper
```

**How it works:**
- Каждый раз, когда вызывается функция, декорированная `@logging_decorator`, декоратор записывает в лог детали вызова функции и результат.
- Декоратор применяется к функциям ``multiply`` и ``greet``:

    ```python
    @logging_decorator
    def multiply(a: int, b: int) -> int:
        return a * b

    @logging_decorator
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"
    ```

  При запуске следующего кода:

    ```python
    result1 = multiply(3, 4)
    result2 = greet("Vadik", greeting="You're welcome")
    ```

  Вывод будет:

    ```
    Calling function 'multiply' with arguments: (3, 4) and keyword arguments: {}
    Function 'multiply' returned: 12

    Calling function 'greet' with arguments: ('Vadik',) and keyword arguments: {'greeting': "You're welcome"}
    Function 'greet' returned: You're welcome, Vadik!
    ```

## Заключение

Декораторы в Python предоставляют мощный механизм для изменения или расширения поведения функций чистым и многократно используемым способом. 
