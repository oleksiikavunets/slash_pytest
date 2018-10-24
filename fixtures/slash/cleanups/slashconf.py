import slash


def a():
    print("\ncleanup itself_1")
    return


def b():
    print("\nyield")
    return


# plain cleanup version 1
@slash.fixture()
def fixture_1(this):
    print("\nbefore cleanup_1")
    this.add_cleanup(a)
    print("\nafter cleanup_1")
    return a


# plain cleanup version 2
@slash.fixture()
def fixture_2(this):
    print("\nbefore cleanup_2")

    @this.add_cleanup
    def cleanup():
        print("\ncleanup itself_2")
    print("\nafter cleanup_2")
    return a


# yielding cleanup
@slash.fixture()
def fixture_3():
    print("\nbefore yield")
    yield
    print("\njust after yield")
