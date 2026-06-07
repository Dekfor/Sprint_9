from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOGIN_TITLE = (By.XPATH,"//h1[contains(text(), 'Войти на сайт')]")

    EMAIL_INPUT = (By.NAME,"email")
    PASSWORD_INPUT = (By.NAME,"password")

    LOGIN_BUTTON = (By.XPATH,"//button[contains(., 'Войти')]")

    LOGIN_FORM = (By.TAG_NAME,"form")
    