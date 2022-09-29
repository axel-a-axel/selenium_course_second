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

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[1]')
    CART_PRICE = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_IN_CART_NAME = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
    ADDED_TO_CART_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')

class BasketPageLocators():
    EMPTY_CART_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')