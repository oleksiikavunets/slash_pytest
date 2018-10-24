import slash

class TestFixtModule(slash.Test):

    @slash.use_fixtures(['usr_netw'])
    def test_assert_netw(self, usr_netw):
        print("\nfixture:\n network =", usr_netw)
        assert usr_netw == {'Olga': '172.31.239.131',
                            'Kvitka': '172.31.239.132',
                            'Olexiy': '172.31.239.133'}

    @slash.use_fixtures(['usr_keys'])
    def test_assert_keys(self, usr_keys):
        keys = usr_keys
        print("\nkeys =", keys)
        assert keys == ['Olga', 'Kvitka', 'Olexiy']

    @slash.use_fixtures(['usr_values'])
    def test_assert_values(self, usr_values):
        values = usr_values
        print("\ntest values(ips) =", values)
        assert values == ['172.31.239.131', '172.31.239.132', '172.31.239.133']


