"""A simple command-line Python application."""


def greet(name: str = "World") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers safely."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def check_even_odd(number: int) -> str:
    """Check whether a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"


def multiplication_table(number: int) -> None:
    """Print the multiplication table of a number."""
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


def get_number(prompt: str) -> float:
    """Read a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu() -> None:
    """Display the application menu."""
    print("\n===== PYTHON MINI APP =====")
    print("1. Greet")
    print("2. Add two numbers")
    print("3. Subtract two numbers")
    print("4. Multiply two numbers")
    print("5. Divide two numbers")
    print("6. Check Even or Odd")
    print("7. Multiplication Table")
    print("8. Exit")


def main() -> None:
    """Run the application."""
    name = input("What is your name? ").strip() or "World"
    print(greet(name))

    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            print(greet(name))

        elif choice in ("2", "3", "4", "5"):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")

            if choice == "2":
                print("Result:", add(a, b))
            elif choice == "3":
                print("Result:", subtract(a, b))
            elif choice == "4":
                print("Result:", multiply(a, b))
            else:
                try:
                    print("Result:", divide(a, b))
                except ValueError as error:
                    print("Error:", error)

        elif choice == "6":
            number = int(get_number("Enter an integer: "))
            print(f"{number} is {check_even_odd(number)}.")

        elif choice == "7":
            number = int(get_number("Enter a number: "))
            multiplication_table(number)

        elif choice == "8":
            print(f"Goodbye, {name}! Thanks for using the app.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 8.")


if __name__ == "__main__":
    main()
