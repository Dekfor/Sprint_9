import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import BASE_URL


class MainPage(BasePage):
    @allure.step("Открыть главную сайта")
    def open(self):
        self.open_url(BASE_URL)

    @allure.step("Нажать 'Создать аккаунт'")
    def click_create_account(self):
        self.click(MainPageLocators.CREATE_ACCOUNT_BUTTON)

    @allure.step("Нажать 'Войти'")
    def click_login(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Нажать 'Создать рецепт'")
    def click_create_recipe(self):
        self.click(MainPageLocators.CREATE_RECIPE_TAB)

    @allure.step("Проверить, что кнопка 'Выйти' отображается")
    def logout_button_visible(self):
        return self.is_visible(MainPageLocators.LOGOUT_BUTTON)
    