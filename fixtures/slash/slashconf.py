import slash


@slash.fixture(autouse=True)
def fixture_1():
    print("\nfixture_1")


@slash.fixture(scope='session')
def fixture_2():
    print("\nfixture_2")


@slash.fixture()
def fixture_3():
    print("\nfixture_3")
