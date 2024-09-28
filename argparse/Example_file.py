import argparse

# ---------------- Example 1 ------------------------

parser = argparse.ArgumentParser(description="Add two numbers")

parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")

args = parser.parse_args()

result = args.num1 + args.num2
print(f"The sum is: {result}")

# ---------------- Example 2 ------------------------

parser = argparse.ArgumentParser(description="Calculator for basic operations")

parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")

parser.add_argument(
    "--operation",
    choices=["add", "subtract", "multiply", "divide"],
    default="add",
    help="Operation to perform (default: add)",
)

args = parser.parse_args()

if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2
elif args.operation == "multiply":
    result = args.num1 * args.num2
elif args.operation == "divide":
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        raise ValueError("Cannot divide by zero")

print(f"The result of {args.operation} operation is: {result}")

# ---------------- Example 3 ------------------------

parser = argparse.ArgumentParser(description="Calculator with verbose mode")

parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")

parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

args = parser.parse_args()

result = args.num1 + args.num2

if args.verbose:
    print(f"Adding {args.num1} and {args.num2}")
print(f"Result: {result}")
