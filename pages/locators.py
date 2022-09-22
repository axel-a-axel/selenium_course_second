from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')

class LoginPageLocators():
    LOGIN_EMAIL = (By.XPATH, '//input[@name="login-username"]')
    LOGIN_PASSWORD = (By.XPATH, '//input[@name="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')

    REGISTER_EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_PASSWORD = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')