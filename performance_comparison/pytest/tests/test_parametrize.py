import pytest


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (2, 3)])
@pytest.mark.pytest_parametrize
def test_parametrize(x, y):
    assert x == y
