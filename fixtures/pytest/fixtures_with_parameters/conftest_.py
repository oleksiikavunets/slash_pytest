import pytest

@pytest.fixture
def usr_netw():
    dict = {'Olga': '172.31.239.131',
            'Kvitka': '172.31.239.132',
            'Olexiy': '172.31.239.133'}
    return dict

@pytest.fixture
def usr_keys(usr_netw):
    print("\nfixture keys (names) = ",usr_netw.keys())
    return list(usr_netw.keys())

@pytest.fixture
def usr_values(usr_netw):
    print("\nfixture values(ips) = ",usr_netw.values())
    return list(usr_netw.values())

@pytest.fixture(params = [
    'Max', '172.31.239.134'
])
def add_netw(request, usr_netw):
    usr_netw[request.param[0]] =request.param[1]
    print("\nfixture new netw = ",usr_netw)
    return usr_netw
