import slash


class Fixtures(slash.Test):

    def test_1(self):
        print("\ntest_1")
        assert 1 == 1

    @slash.use_fixtures(['fixture_2'])
    def test_2(self):
        print("\ntest_2")
        assert 1 == 1

    def test_3(self, fixture_3):
        print("\ntest_3")
        assert 1 == 1

