import slash


@slash.fixture()
def fixture_1():
    print("\nfixture_1")


@slash.fixture(autouse=True)
def fixture_2(fixture_1):
    print("\nfixture_2")


class Tests(slash.Test):

    # will use both fixtures
    def test_1(self):
        print("\ntest_1")
        assert 1 == 1
