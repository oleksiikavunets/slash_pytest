import pytest

@pytest.mark.usefixtures('fixture_1', 'fixture_2')
class Tests:

    def test_1(self):
        print("\ntest_1")
        assert 1 == 1

    def test_2(self):
        print("\ntest_2")
        assert 1 == 1

