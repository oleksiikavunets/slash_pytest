import slash

@slash.fixture
@slash.parametrize('local',['172.31.239.134', '172.31.239.135'])
def connect(local):
    print()
    print("...connecting to ", local)
    return local