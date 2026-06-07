from selenium.webdriver.common.by import By


class RecipePageLocators:

    RECIPE_NAME = (By.XPATH,"(//input[contains(@class,'styles_inputField')])[1]")
    INGREDIENT_INPUT = (By.CSS_SELECTOR,".styles_ingredientsInput__1zzql")
    INGREDIENT_AMOUNT = (By.CSS_SELECTOR,".styles_ingredientsAmountValue__2matT")
    ADD_INGREDIENT_BUTTON = (By.XPATH,"//div[contains(text(),'Добавить ингредиент')]")
    FIRST_INGREDIENT_FROM_LIST = (By.XPATH,"//div[contains(@class,'styles_container__3ukwm')]/div[1]")
    COOK_TIME = (By.XPATH,"//div[contains(text(),'Время приготовления')]/following::input[1]")
    DESCRIPTION = (By.TAG_NAME,"textarea")
    FILE_INPUT = (By.CSS_SELECTOR,"input[type='file']")

    CREATE_RECIPE_BUTTON = (By.XPATH,"//button[contains(text(),'Создать рецепт')]")

    RECIPE_CARD = (By.XPATH,"//div[contains(@class,'styles_single-card')]")
    RECIPE_TITLE = (By.XPATH,"//h1[contains(@class,'styles_single-card__title')]")
    