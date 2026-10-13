"""A small command-line Python application."""




def main() -> None:
    """Run the application."""
    name = input("What is your name? ").strip() or "World"
    print(greet(name))


if __name__ == "__main__":
    main()
