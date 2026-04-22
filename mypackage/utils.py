"""Utility functions for mypackage."""


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, ignores spaces)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
