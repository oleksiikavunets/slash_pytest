import pytest

# overrides fixture from conftest.py
@pytest.fixture
def fixture_1(fixture_1):
    return 'overriden-' + fixture_1


@pytest.fixture(params=['1', '2', '3'])
def fixture_2(request):
    return request.param


class Tests:

    def test_1(self, fixture_1):
        assert fixture_1 == 'overriden-to override'

    def test_2(self, fixture_2):
        print("\n{0}".format(fixture_2))
        assert 1 == 1

