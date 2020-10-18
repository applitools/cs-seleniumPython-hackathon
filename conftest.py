import pytest

def pytest_addoption(parser):
    parser.addoption("--url", action="store", help="test url")
@pytest.fixture
def params(request):
    params = {}
    params['url'] = request.config.getoption('--url')
    if params['url'] is None:
        pytest.skip()
    return params