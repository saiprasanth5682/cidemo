"""Small sample Python application for practicing CI workflows."""

def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def greet(name: str) -> str:
    """Return a simple greeting."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("Name cannot be empty.")
    return f"Hello, {cleaned_name}!"

if __name__ == "__main__":
    print(greet("Vijay"))
    print(f"10 + 20 = {add_numbers(10, 20)}")
