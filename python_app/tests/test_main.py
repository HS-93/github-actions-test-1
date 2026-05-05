import pytest

from app import main


def test_add():
    assert main.add(2, 3) == 6
