# Library `argparse` in Python

`argparse` — это стандартная библиотека в Python, которая используется для создания программ с интерфейсом командной строки. Она позволяет парсить переданные пользователем аргументы при запуске программы, что делает программу более интерактивной и гибкой. Это особенно полезно для автоматизации задач, создания утилит или CLI-интерфейсов.

## Зачем использовать `argparse`?

- Позволяет легко управлять входными данными через командную строку.
- Программа может принимать различные аргументы и изменять своё поведение на их основе.
- Позволяет автоматически генерировать помощь (`--help`), что упрощает использование программы.

## Основные компоненты:

1. **Позиционные аргументы** — обязательные аргументы, которые нужно передать в определённом порядке.
2. **Опциональные аргументы** — необязательные аргументы, которые можно задавать с помощью флагов (например, `--verbose`).
3. **Параметры и типы аргументов** — можно задать, какие именно типы данных ожидаются на входе (например, `int`, `str`).

## Пример использования:

### 1. Базовый пример

Этот пример программы принимает два числа и выводит их сумму:

```python
import argparse

parser = argparse.ArgumentParser(description="Add two numbers")

parser.add_argument('num1', type=int, help="First number")
parser.add_argument('num2', type=int, help="Second number")

args = parser.parse_args()

result = args.num1 + args.num2
print(f"The sum is: {result}")
```

**How to use:**
```bash
$ python script.py 5 10
The sum is: 15
```

Здесь:
- `num1` и `num2` — обязательные позиционные аргументы.
- Программа выводит их сумму.

### 2. Пример с опциональными аргументами

Теперь добавим опциональный аргумент для выбора операции (сложение, вычитание, умножение, деление):

```python
import argparse

parser = argparse.ArgumentParser(description="Calculator for basic operations")

parser.add_argument('num1', type=int, help="First number")
parser.add_argument('num2', type=int, help="Second number")

parser.add_argument('--operation', choices=['add', 'subtract', 'multiply', 'divide'], default='add', help="Operation to perform (default: add)")

args = parser.parse_args()

if args.operation == 'add':
    result = args.num1 + args.num2
elif args.operation == 'subtract':
    result = args.num1 - args.num2
elif args.operation == 'multiply':
    result = args.num1 * args.num2
elif args.operation == 'divide':
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        raise ValueError("Cannot divide by zero")

print(f"The result of {args.operation} operation is: {result}")
```

**How to use:**
```bash
$ python script.py 8 4 --operation add
The result of add operation is: 12

$ python script.py 8 4 --operation divide
The result of divide operation is: 2.0

$ python script.py 8 4
The result of add operation is: 12
```

Здесь:
- Мы добавили опциональный аргумент `--operation`, который позволяет выбрать операцию.
- Если пользователь не укажет операцию, по умолчанию будет выполнено сложение.

### 3. Пример с флагами

Теперь добавим флаг, который изменяет поведение программы, например, включает "verbose" режим:

```python
import argparse

parser = argparse.ArgumentParser(description="Calculator with verbose mode")

parser.add_argument('num1', type=int, help="First number")
parser.add_argument('num2', type=int, help="Second number")

parser.add_argument('--verbose', action='store_true', help="Enable verbose mode")

args = parser.parse_args()

result = args.num1 + args.num2

if args.verbose:
    print(f"Adding {args.num1} and {args.num2}")
print(f"Result: {result}")
```

**How to use:**
```bash
$ python script.py 3 7
Result: 10

$ python script.py 3 7 --verbose
Adding 3 and 7
Result: 10
```

Здесь:
- `--verbose` — это флаг, который активируется, если он указан в командной строке.
- Если включён режим "verbose", программа дополнительно выводит детали операции.

## Использование `argparse` в реальных проектах

1. **CLI-инструменты**:
   `argparse` часто используется для создания утилит командной строки, которые упрощают взаимодействие пользователя с программой. Например, такие программы, как `git`, `docker` или `pip`, поддерживают множество опций и параметров, и такая структура легко реализуема с помощью `argparse`.

2. **Автоматизация задач**:
   Если вы пишете Python-скрипты для автоматизации задач (например, для обработки файлов, работы с базами данных или API), `argparse` позволяет вам гибко управлять входными данными и результатами выполнения программы через командную строку.

3. **Скрипты для администрирования**:
   В администрировании серверов часто пишут Python-скрипты для управления системами, резервного копирования или мониторинга. `argparse` помогает конфигурировать эти скрипты и предоставлять гибкий интерфейс для настройки.

## Автоматическая генерация помощи

Одним из удобных преимуществ `argparse` является автоматическая генерация справки по использованию программы. Если пользователь запустит скрипт с флагом `--help`, программа выведет описание всех доступных опций.

```bash
$ python script.py --help
usage: script.py [-h] [--verbose] num1 num2

Calculator with verbose mode

positional arguments:
  num1        First number
  num2        Second number

optional arguments:
  -h, --help  show this help message and exit
  --verbose   Enable verbose mode
```

## Заключение

`argparse` — это мощный инструмент для создания программ с интерфейсом командной строки. Он позволяет легко управлять вводом данных через аргументы, которые пользователь передает при запуске программы. Среди основных преимуществ использования `argparse`:
- Автоматическая обработка аргументов.
- Поддержка позиционных и опциональных аргументов.
- Легкость в создании профессионального CLI-интерфейса.
