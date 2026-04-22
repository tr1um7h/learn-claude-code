"""Tests for mypackage.utils."""

import pytest

from mypackage.utils import greet, add, is_palindrome


class TestGreet:
    def test_greet_with_name(self):
        assert greet("World") == "Hello, World!"

    def test_greet_with_empty_string(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")

    def test_greet_with_spaces(self):
        assert greet("Python Dev") == "Hello, Python Dev!"


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_add_zero(self):
        assert add(0, 0) == 0


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_with_mixed_case(self):
        assert is_palindrome("RaceCar") is True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_empty_string(self):
        assert is_palindrome("") is True
