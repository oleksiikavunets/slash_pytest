import slash

@slash.fixture ##(scope="module")
def usr_netw():
    return {'Olga': '172.31.239.131',
            'Kvitka': '172.31.239.132',
            'Olexiy': '172.31.239.133'}

# @pytest.fixture
# def usr_netw_print(usr_netw):
#     print(usr_netw)


@slash.fixture
def usr_keys(usr_netw):
    print("\nfixture keys (names) = ",usr_netw.keys())
    return list(usr_netw.keys())

@slash.fixture
def usr_values(usr_netw):
    print("\nfixture values(ips) = ",usr_netw.values())
    return list(usr_netw.values())
