from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url f'expected login to be substring of {self.browser.current_url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), 'Login: Email field is not present'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'Login: Password field is not present'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Login: Button is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), 'Registration: Email field is not present'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), 'Registration: Password field is not present'
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), 'Registration: Confirm password field is not present'
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), 'Registration: Button is not present'