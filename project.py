def add(x: float, y: float) -> float:
    """Return the sum of two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Return the difference of two numbers."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Return the product of two numbers."""
    return x * y


def divide(x: float, y: float) -> float:
    """Return the quotient of two numbers. Raise ValueError if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def main():
    print("Welcome to CS50 Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == "5":
            print("Exiting Calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        try:
            if choice == "1":
                print(f"Result: {add(x, y)}")
            elif choice == "2":
                print(f"Result: {subtract(x, y)}")
            elif choice == "3":
                print(f"Result: {multiply(x, y)}")
            elif choice == "4":
                print(f"Result: {divide(x, y)}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
