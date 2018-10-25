import pytest
##requires pytest-lazy-fixture plugin !!

# @pytest.fixture
# def sample_foo_with_bar1_and_baz2():
#     return 'fixture_with_a_very_long_name'
#
#
# @pytest.mark.parametrize('foo',
#                          [pytest.lazy_fixture('sample_foo_with_bar1_and_baz2')])
# def test_foo_with_bar1_and_baz2(foo):
#     assert 'fixture_with_a_very_long_name' == foo

##########
@pytest.fixture
def ips():
    return ['172.31.239.131',
            '172.31.239.132',
            '172.31.239.133']

@pytest.fixture
def load_main_page(ips):
    return "\nload main_page: "+ips[0]


@pytest.fixture
def load_login_page(ips):
    return "\nload login page: "+ips[1]


@pytest.fixture
def load_contacts_page(ips):
    return "\nload contact page: "+ips[2]

@pytest.mark.parametrize('lmp',
                         [pytest.lazy_fixture('load_main_page')])
def test_load_main(lmp):
    print(lmp)

@pytest.mark.parametrize('llp',
                         [pytest.lazy_fixture('load_login_page')])
def test_load_main(llp):
    print(llp)

@pytest.mark.parametrize('lcp',
                         [pytest.lazy_fixture('load_contacts_page')])
def test_load_main(lcp):
    print(lcp)


#
#
# def test_load_login(llp: pytest.use('load_login_page')):
#     print(llp)
#
# def test_load_contacts(lcp: pytest.use('load_contacts_page')):
#     print(lcp)