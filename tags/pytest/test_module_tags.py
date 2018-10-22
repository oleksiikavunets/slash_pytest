import pytest

pytestmark = pytest.mark.module_tag


def test_tags_a():
    assert 1 == 1


def test_tags_b():
    assert 1 == 1


def test_tags_c():
    assert 1 == 1
