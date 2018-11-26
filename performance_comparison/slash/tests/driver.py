import slash
from selenium.webdriver import Chrome


@slash.tag('slash_driver')
@slash.repeat(100)
def test_driver():
    driver = Chrome()
    driver.get('about:blank')
    driver.quit()
