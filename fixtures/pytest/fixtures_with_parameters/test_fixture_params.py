import pytest


# @pytest.fixture
# def usr_netw():
#     dict = {'Olga': '172.31.239.131',
#             'Kvitka': '172.31.239.132',
#             'Olexiy': '172.31.239.133'}
#     return dict

dict = {'Olga': '172.31.239.131',
        'Kvitka': '172.31.239.132',
        'Olexiy': '172.31.239.133'}

@pytest.fixture(params = [
    'Max', '172.31.239.134'
])
def add_netw(request, usr_netw):
    usr_netw.update(request.param[0], request.param[1])
    print("\nfixture new netw = ",usr_netw)
    return usr_netw

class TestFixtModule:

    def test_assert_netw(self, usr_netw):
        print("type netw : ",type(usr_netw))
        print("\nfixture:\n network =", usr_netw)
        assert usr_netw == {'Olga': '172.31.239.131',
                            'Kvitka': '172.31.239.132',
                            'Olexiy': '172.31.239.133'}

    # def usr_netw(self, request):
    #     print(type(request.param))
    #     # print("param[0]: ",request.param[0])
    #     # print("param[1]: ",request.param[1])
    #     #d = dict(request.param)
    #     return request.param

    # def test_assert_netw(self, usr_netw):
    #     add_netw(self, usr_netw)
    #     print(type(usr_netw))
    #     print("\nfixture:\n network =", usr_netw)
     #    assert usr_netw == [
     #    ('Olga', '172.31.239.131'),
     #    ('Kvitka', '172.31.239.132'),
     #    ('Olexiy', '172.31.239.133')
     # ]