import slash


@slash.fixture()
def fixture_1(this):
    print("\nfixture_1")

    @this.test_start
    def on_test_start():
        print("\nstart")

    @this.test_end
    def on_test_end():
        print("\nend")


class Tests(slash.Test):

    def test_1(self, fixture_1):
        print("\ntest_1")