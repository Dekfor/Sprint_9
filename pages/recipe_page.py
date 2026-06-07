import allure
from pathlib import Path
from pages.base_page import BasePage
from data.recipe import RecipeData
from locators.recipe_page_locators import (RecipePageLocators)


class RecipePage(BasePage):

    @allure.step("Создать рецепт")
    def create_recipe(self,recipe_name,description):

        self.fill(RecipePageLocators.RECIPE_NAME,recipe_name)
        self.fill(RecipePageLocators.INGREDIENT_INPUT, RecipeData.INGREDIENT_QUERY)
        self.click(RecipePageLocators.FIRST_INGREDIENT_FROM_LIST)
        self.fill(RecipePageLocators.INGREDIENT_AMOUNT, RecipeData.INGREDIENT_AMOUNT)
        self.click(RecipePageLocators.ADD_INGREDIENT_BUTTON)
        self.fill(RecipePageLocators.COOK_TIME, RecipeData.COOK_TIME)
        self.fill(RecipePageLocators.DESCRIPTION,description)

        image_path = Path(__file__).parent.parent / "assets" / RecipeData.IMAGE_NAME
        self.find_present(RecipePageLocators.FILE_INPUT).send_keys(str(image_path))

        self.click(RecipePageLocators.CREATE_RECIPE_BUTTON)

    @allure.step("Проверить, что карточка созданного рецепта отображается")
    def recipe_card_visible(self):
        return self.is_visible(RecipePageLocators.RECIPE_CARD)
    
    @allure.step("Проверить название, которое заполняли при создании")
    def get_recipe_title(self):
        return self.get_text(RecipePageLocators.RECIPE_TITLE)
    