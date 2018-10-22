import pytest


@pytest.mark.method_tag_1
def test_tags_a():
    assert 1 == 1


@pytest.mark.method_tag_2
def test_tags_b():
    assert 1 == 1


@pytest.mark.parametrize(("actual", "expected"), [
    (1, 1),
    pytest.mark.method_tag_1((2, 2)),
    (3, 3)
])
def test_tags_c(actual, expected):
    assert actual == expected