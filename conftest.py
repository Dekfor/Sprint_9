import pytest, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    selenoid_url = os.getenv("SELENOID_URL")
    options = Options()
    options.add_argument("--window-size=1920,1080")

    if selenoid_url:
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")

        driver = webdriver.Remote(command_executor=selenoid_url,options=options)
    else:
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
