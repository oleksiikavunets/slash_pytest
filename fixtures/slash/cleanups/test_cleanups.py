import slash


class Fixtures(slash.Test):

    def test_1(self, fixture_1):
        print("\ntest_1")
        assert 1 == 1

    def test_2(self, fixture_2):
        print("\ntest_2")
        assert 1 == 1

    def test_3(self, fixture_3):
        print("\ntest_3")
        assert 1 == 1

