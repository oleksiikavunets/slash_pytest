import pytest


@pytest.fixture
def fixture_1():
    a = 'to override'
    return a