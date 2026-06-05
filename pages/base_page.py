from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();",element)

    def fill(self, locator, value):
        element = self.find(locator)

        element.clear()
        element.send_keys(value)
    
    def find_present(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        return self.find(locator).is_displayed()

    def get_current_url(self):
        return self.driver.current_url
    