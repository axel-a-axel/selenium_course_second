from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    ''' seems to be excess and pointless
    def should_be_added_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_CART_MESSAGE), 'No add to cart message found'
    '''

    def should_be_same_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert product_price == cart_price, f'Expected {product_price=} to be equal to {cart_price=}'

    def should_be_same_product_names(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        cart_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_NAME).text
        assert product_name == cart_name, f'Expected {product_name=} to be equal to {cart_name=}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_CART_MESSAGE), 'Added to cart message is present, but it should not be'

    def should_not_be_success_message_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_CART_MESSAGE), 'Added to cart message is present, but it should dissappear'

