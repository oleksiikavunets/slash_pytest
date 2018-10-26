import slash


@slash.fixture()
def fixture1():
    print("Run fixture 1\n")

@slash.fixture()
def fixture2():
    print("Run fixture 2\n")

@slash.fixture()
def fixture3():
    print("Run fixture 3\n")

@slash.fixture()
def fixture4():
    print("Run fixture 4\n")

@slash.fixture()
def fixture5():
    print("Run fixture 5\n")

# @slash.use_fixtures(["fixture1", "fixture2"])
# def test_fixture_1_2():
#     print("Runned fixtures 1,2\n##########\n")
#
#
# @slash.use_fixtures(["fixture2", "fixture1"])
# def test_fixture_2_1():
#     print("Runned fixtures 2,1\n##########\n")
#
# @slash.use_fixtures(["fixture1", "fixture3"])
# def test_fixture_1_3():
#     print("Runned fixtures 1,3\n##########\n")
#
# @slash.use_fixtures(["fixture1", "fixture2", "fixture3"])
# def test_three_fixtures():
#     print("Run all fixtures 1,2,3:\n##########\n")

@slash.use_fixtures(["fixture1", "fixture2", "fixture3", "fixture4", "fixture5"])
def test_all_fixturesa():
    print("Run all fixtures (1-st time) 1,2,3,4,5:\n##########\n")

@slash.use_fixtures(["fixture1", "fixture2", "fixture3", "fixture4", "fixture5"])
def test_all_fixturesb():
    print("Run all fixtures (1-st time) 1,2,3,4,5:\n##########\n")

@slash.use_fixtures(["fixture1", "fixture2", "fixture3", "fixture4", "fixture5"])
def test_all_fixturesc():
    print("Run all fixtures (1-st time) 1,2,3,4,5:\n##########\n")


