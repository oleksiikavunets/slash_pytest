import pytest


@pytest.fixture(autouse=True)
def fixture_1():
    print("\nfixture_1")


@pytest.fixture(scope='session')
def fixture_2():
    print("\nfixture_2")


@pytest.fixture()
def fixture_3():
    print("\nfixture_3")