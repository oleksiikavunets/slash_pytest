import slash

@slash.fixture
def ips():
    return ['172.31.239.131',
            '172.31.239.132',
            '172.31.239.133']

@slash.fixture
def load_main_page(ips):
    return "\nload main_page: "+ips[0]


@slash.fixture
def load_login_page(ips):
    return "\nload login page: "+ips[1]


@slash.fixture
def load_contacts_page(ips):
    return "\nload contact page: "+ips[2]

def test_load_main(lmp: slash.use('load_main_page')):
    print(lmp)

def test_load_login(llp: slash.use('load_login_page')):
    print(llp)

def test_load_contacts(lcp: slash.use('load_contacts_page')):
    print(lcp)