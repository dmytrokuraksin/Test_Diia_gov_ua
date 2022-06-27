from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time




class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.shoud_be_button_basket()
        self.solve_quiz_and_get_code()
        # time.sleep(5)
        self.product_in_basket_is_right()
        # time.sleep(5)

    def shoud_be_button_basket (self):
        # name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        # return name_book
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()


    def product_in_basket_is_right (self):
        # view_basket = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        # view_basket.click()
        self.should_be_right_book()
        self.should_be_right_price()
        # assert "9.99" in self.browser.find_element(*ProductPageLocators.PRICE).text, "Price is not correct"

    def should_be_right_book(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == name_book, "Name is dismiss"

    def should_be_right_price(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_TOTAL).text
        assert product_price == price_book, "Price is dismiss"
        


        