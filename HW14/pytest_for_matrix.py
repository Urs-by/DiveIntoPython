from homework14 import Matrix, MyExceptionMultMatrix, MyExceptionAddMatrix

import pytest


@pytest.fixture
def m1():
    return Matrix([[1, 2], [3, 4]])


@pytest.fixture
def m2():
    return Matrix([[1, 2], [3, 4]])


@pytest.fixture
def m3():
    return Matrix([[7, 8], [9, 1], [2, 3]])


def test_eq(m1, m2):
    assert m1 == m2


def test_add(m1, m2):
    assert m1 + m2 == Matrix([[2, 4], [6, 8]]), "Матрицы не равны"


def test_mult(m1, m2):
    assert m1 * m2 == Matrix([[7, 10], [15, 22]])


def test_add_size_matrix(m1, m3):
    with pytest.raises(MyExceptionAddMatrix):
        assert m1 + m3


def test_mult_size_matrix(m1, m3):
    with pytest.raises(MyExceptionMultMatrix):
        assert m1 * m3


if __name__ == "__main__":
    pytest.main()
