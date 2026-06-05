import allure
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from data.registration import (generate_user_data)


class TestRegistration:

    @allure.title("Создание аккаунта")
    def test_create_account(self,driver):
        user = generate_user_data()

        main_page = MainPage(driver)
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.click_create_account()

        register_page.fill_registration_form(user)
        register_page.click_create_account()

        assert "/signin" in (login_page.get_current_url())

        assert (login_page.login_form_visible())
        