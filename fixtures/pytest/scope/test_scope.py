import pytest


# works once per module
@pytest.fixture(scope='module')
def fixture_3():
    print("\nfixture_3")


@pytest.mark.usefixtures('fixture_4', 'fixture_3')
class Tests:

    def test_1(self):
        print("\ntest_1")
        assert 1 == 1

    @pytest.mark.usefixtures('fixture_2')
    def test_2(self):
        print("\ntest_2")
        assert 1 == 1

    def test_3(self, fixture_3):
        print("\ntest_3")
        assert 1 == 1

    def test_4(self, fixture_5):
        print("\ntest_4")
        assert 1 == 1

