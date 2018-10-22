import pytest


@pytest.mark.class_tag
class TestClassTags:
    def test_tags_a(self):
        assert 1 == 1

    def test_tags_b(self):
        assert 1 == 1

    def test_tags_c(self):
        assert 1 == 1
