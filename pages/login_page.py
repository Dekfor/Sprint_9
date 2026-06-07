import allure
from pages.base_page import BasePage
from locators.login_page_locators import (LoginPageLocators)

class LoginPage(BasePage):
    @allure.step("Авторизоваться")
    def login(self, username, password):

        self.fill(LoginPageLocators.EMAIL_INPUT,username)
        self.fill(LoginPageLocators.PASSWORD_INPUT,password)

        self.click(LoginPageLocators.LOGIN_BUTTON)

        self.wait_url_contains("/recipes")

    @allure.step("Проверить, что форма авторизации отображается")
    def login_form_visible(self):
        return self.is_visible(LoginPageLocators.LOGIN_FORM)
    
    @allure.step("Проверить, что заголовок страницы авторизации отображается")
    def login_title_visible(self):
        return self.is_visible(LoginPageLocators.LOGIN_TITLE)
    