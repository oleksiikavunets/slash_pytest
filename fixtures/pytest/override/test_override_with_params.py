import pytest


# overrides parametrized fixture from other class with non-parametrized
@pytest.fixture()
def fixture_2():
    return "remove params"


class Tests:

    def test_1(self, fixture_2):
        assert fixture_2 == "remove params"