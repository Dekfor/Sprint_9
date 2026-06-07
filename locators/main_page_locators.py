from selenium.webdriver.common.by import By


class MainPageLocators:

    CREATE_ACCOUNT_BUTTON = (By.XPATH,"//a[@href='/signup']")
    LOGIN_BUTTON = (By.XPATH,"//a[@href='/signin']")
    LOGOUT_BUTTON = (By.XPATH,"//a[contains(text(),'Выход')]")
    CREATE_RECIPE_TAB = (By.XPATH,"//a[@href='/recipes/create']")
    