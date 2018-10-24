import pytest


def a():
    print("\ncleanup itself")
    return


def b():
    print("\nyield")
    return


# plain cleanup with 'addfinalizer'
@pytest.fixture()
def fixture_1(request):
    print("\nbefore cleanup")

    def cleanup():
        a()

# works regardless if the fixture setup code raises an exception
    request.addfinalizer(cleanup)

    print("\nafter cleanup")
    return


# yielding cleanup
@pytest.fixture()
def fixture_2():
    print("\nbefore yield")
    yield
    print("\nafter yield")

