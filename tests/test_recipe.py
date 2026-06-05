import random, allure
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.recipe_page import RecipePage
from pages.main_page import MainPage
from data.registration import (generate_user_data)


class TestRecipe:

    @allure.title("Создание рецепта")
    def test_create_recipe(self,driver):
        user = generate_user_data()

        recipe_name = (f"Рецепт_{random.randint(1,99999)}")

        main_page = MainPage(driver)
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)
        recipe_page = RecipePage(driver)

        main_page.open()
        main_page.click_create_account()

        register_page.fill_registration_form(user)
        register_page.click_create_account()

        login_page.login(user["username"],user["password"])

        main_page.click_create_recipe()

        recipe_page.create_recipe(recipe_name,"Описание")

        assert (recipe_page.recipe_card_visible())
        assert (recipe_page.get_recipe_title()== recipe_name)

