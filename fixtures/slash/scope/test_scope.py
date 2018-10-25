import slash


# works per module
@slash.fixture(autouse=True, scope='module')
def fixture_3():
    print("\nfixture_3")


class Fixtures(slash.Test):

    def test_1(self):
        print("\ntest_1")
        assert 1 == 1

    @slash.use_fixtures(['fixture_4'])
    def test_2(self):
        print("\ntest_2")
        assert 1 == 1

    def test_3(self):
        print("\ntest_3")
        assert 1 == 1

    def test_4(self):
        print("\ntest_4")
        assert 1 == 1
