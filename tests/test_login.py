import allure
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from data.registration import (generate_user_data)


class TestLogin:

    @allure.title("Авторизация пользователя")
    def test_login(self,driver):
        user = generate_user_data()

        main_page = MainPage(driver)
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.click_create_account()

        register_page.fill_registration_form(user)
        register_page.click_create_account()

        login_page.login(user["username"],user["password"])

        assert "/recipes" in (login_page.get_current_url())
        assert (main_page.logout_button_visible())
