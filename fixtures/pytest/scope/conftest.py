import pytest


# works every time any test is executed
@pytest.fixture(autouse=True)
def fixture_1():
    print("\nfixture_1")


# works once per any session run
@pytest.fixture(autouse=True, scope='session')
def fixture_2():
    print("\nfixture_2")


# works once per assigned class
@pytest.fixture(scope='class')
def fixture_4():
    print("\nfixture_4")


# works once per assigned test
@pytest.fixture(scope='function')
def fixture_5():
    print("\nfixture_5")


# works once per package
@pytest.fixture(autouse=True, scope='package')
def fixture_6():
    print("\nfixture_6")
