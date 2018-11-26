import pytest
from selenium.webdriver import Chrome


@pytest.mark.pytest_driver
def test_driver():
    driver = Chrome()
    driver.get('about:blank')
    driver.quit()
