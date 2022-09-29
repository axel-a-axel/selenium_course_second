from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert 'Your basket is empty.' in self.browser.find_element(*BasketPageLocators.EMPTY_CART_MESSAGE).text, 'empty basket message not found'