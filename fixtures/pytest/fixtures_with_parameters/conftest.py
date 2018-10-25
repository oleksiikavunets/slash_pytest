import pytest

@pytest.fixture(params = [('172.31.239.134', '8000')])
def connect(request):
    print("...connecting to ",request.param[0],":",request.param[1])
    return request.param[0],request.param[1]