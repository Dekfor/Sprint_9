import allure
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from locators.register_page_locators import (RegisterPageLocators)


class RegisterPage(BasePage):

    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(self, user):

        self.fill(RegisterPageLocators.FIRST_NAME,user["first_name"])
        self.fill(RegisterPageLocators.LAST_NAME,user["last_name"])
        self.fill(RegisterPageLocators.USERNAME,user["username"])
        self.fill(RegisterPageLocators.EMAIL,user["email"])
        self.fill(RegisterPageLocators.PASSWORD,user["password"])

    @allure.step("Нажать кнопку 'Создать аккаунт'")
    def click_create_account(self):
        self.click(RegisterPageLocators.CREATE_ACCOUNT_BUTTON)
        
        WebDriverWait(self.driver, 10).until(lambda d: "/signin" in d.current_url)
