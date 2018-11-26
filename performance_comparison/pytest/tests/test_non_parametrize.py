import pytest


@pytest.mark.non_parametrize
def test_non_parametrize_1():
    assert 1 == 1


@pytest.mark.non_parametrize
def test_non_parametrize_2():
    assert 2 == 3
