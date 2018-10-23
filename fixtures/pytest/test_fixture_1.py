import pytest

@pytest.fixture
def usr_netw():
    return {'Olga': '172.31.239.131',
            'Kvitka': '172.31.239.132',
            'Olexiy': '172.31.239.133'}

@pytest.fixture
def usr_values(usr_netw):
    print("\nfixture values(ips) = ",usr_netw.values())
    return usr_netw.values()

@pytest.fixture
def usr_keys(usr_netw):
    print("\nfixture keys (names) = ",usr_netw.keys())
    return usr_netw.keys()

def test_assert_netw(usr_netw):
    print("\nfixture:\n network =", usr_netw)
    assert usr_netw == {'Olga': '172.31.239.131',
            'Kvitka': '172.31.239.132',
            'Olexiy': '172.31.239.133'}

def test_assert_keys(usr_netw):
    keys = usr_netw.keys()
    print("\nkeys =", keys)
    assert keys =={'Olga', 'Kvitka', 'Olexiy'}

def test_assert_keys_fixtures(usr_keys):
    keys = usr_keys
    print("\nkeys =", keys)
    assert keys == {'Olga', 'Kvitka', 'Olexiy'}

#  in  progress
# def test_assert_values(usr_values):
#     values = usr_values
#     print("\ntest values(ips) =", values)
#     assert values == {'172.31.239.131',
#                              '172.31.239.132',
#                              '172.31.239.133'}