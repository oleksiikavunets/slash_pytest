import slash


# works every time any test is executed
@slash.fixture(autouse=True)
def fixture_1():
    print("\nfixture_1")


# works once per any session run
@slash.fixture(autouse=True, scope='session')
def fixture_2():
    print("\nfixture_2")


# works only at assigned test
@slash.fixture(scope='test')
def fixture_4():
    print("\nfixture_4")
