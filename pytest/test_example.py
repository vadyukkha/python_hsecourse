import pytest


def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(2, 4) == 6
    assert add(2, 3) == 5
