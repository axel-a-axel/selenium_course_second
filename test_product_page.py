from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage


urls = {'pdp' : ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'],
        'homepage': ['http://selenium1py.pythonanywhere.com/']
        }
urls2 = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/']

@pytest.mark.parametrize('link', urls['pdp'])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    #page.solve_quiz_and_get_code()
    page.should_be_same_price()
    page.should_be_same_product_names()

@pytest.mark.xfail
@pytest.mark.parametrize('link', urls['pdp'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', urls['pdp'])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
@pytest.mark.parametrize('link', urls['pdp'])
def test_message_dissappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', urls['pdp'])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link', urls['pdp'])
def test_guest_can_go_to_login_page_from_product_page (browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.basketpage
@pytest.mark.parametrize('link', urls['homepage'])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):

    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    time.sleep(4)

