import slash

<<<<<<< HEAD:fixtures/slash/slashconf.py
=======

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
>>>>>>> cf5e996a31099057a5582f66ee88e4b5e7d8dcac:fixtures/slash/use_other_fixture/test_use_other_fixture.py
