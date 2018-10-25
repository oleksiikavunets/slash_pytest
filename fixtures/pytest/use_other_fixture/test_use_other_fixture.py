import pytest


@pytest.fixture
def fixture_1():
    print("\nfixture_1")


@pytest.fixture
def fixture_2(fixture_1):
    print("\nfixture_2")


class Tests:

    # will use both fixtures
    def test_1(self, fixture_2):
        print("\ntest_1")