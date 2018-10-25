import pytest

local_ip = ['172.31.239.131',
            '172.31.239.132',
            '172.31.239.133']

@pytest.fixture()
def iter_yield():
    for l in local_ip:
        yield l
        print("current ip: "+l)


def test_yield():
    iter_yield
