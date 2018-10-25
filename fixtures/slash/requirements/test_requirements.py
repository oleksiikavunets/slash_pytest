import slash

a = True


@slash.fixture()
@slash.requires(a, "Requires specific condition")
def fixture_1():
    print("\nfixture_1")


b = False


@slash.fixture()
@slash.requires(b, "Requires specific condition")
def fixture_2():
    print("\nfixture_2")


class Fixtures(slash.Test):

    # will run as fixture requirement is met
    def test_1(self, fixture_1):
        print("\ntest_1")
        assert 1 == 1

    # won't run as fixture requirement is not met
    def test_2(self, fixture_2):
        print("\ntest_2")
        assert 1 == 1
