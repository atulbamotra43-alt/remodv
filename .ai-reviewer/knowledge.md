# remodv reviewer notes

## Architecture
This is a small, standard-library-only Python command-line application. `app.py` contains both reusable arithmetic/helper functions and the interactive menu-driven `main()` loop, while `test_app.py` provides a minimal `unittest` test for the greeting behavior. Execution is guarded by `if __name__ == "__main__":`, so importing `app` does not start the CLI.

## Conventions
- Keep the project dependency-free; `requirements.txt` explicitly states that only Python’s standard library is used.
- Use type annotations and short docstrings for public functions, as shown throughout `app.py` (`greet(name: str) -> str`, `divide(a: float, b: float) -> float`).
- Keep pure operations separate from input/output where practical: arithmetic and validation helpers return values, while `main()`, `show_menu()`, and `multiplication_table()` handle console interaction.
- Use `unittest` for tests, with test classes inheriting from `unittest.TestCase`; see `test_app.py`.
- Preserve the existing user-facing console style: prompts and messages are printed directly, and invalid input is handled with retry loops in `get_number()` and `get_integer()`.
- Use snake_case for functions and variables (`check_even_odd`, `multiplication_table`, `get_integer`) and constants are not currently introduced.

## Intentional non-standard choices
- The application is intentionally a single-file CLI rather than a layered/package structure; `app.py` contains the menu, input handling, business functions, and program entry point.
- User input errors are handled interactively by printing a message and retrying, rather than propagating exceptions or using a CLI argument parser.
- Division by zero intentionally raises `ValueError` in `divide()` and is caught at the menu call site to print `Error: ...`; do not replace this with a silent result or a different exception type without a functional reason.

## Watch out for
- Do not allow `divide()` to return `inf`, `None`, or silently handle a zero denominator; its explicit `ValueError("Cannot divide by zero.")` behavior is part of the current contract.
- Avoid moving `input()` or `print()` into the arithmetic helpers, since callers and tests expect functions such as `add()`, `subtract()`, and `greet()` to be directly usable without console I/O.
- Preserve the `main()` import guard; removing it would make importing `app` from tests launch the interactive application.
- Changes to menu choices must update both `show_menu()` and the corresponding branches and validation message in `main()`.
- New behavior should have focused tests in `test_app.py`; currently only `greet()` is covered, so arithmetic, validation, and menu changes are especially easy to regress.