from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time




class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.shoud_be_button_basket()
        self.solve_quiz_and_get_code()
        self.product_in_basket_is_right()

    def shoud_be_button_basket (self):
        # name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        # return name_book
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def product_in_basket_is_right (self):
        view_basket = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        view_basket.click()
        self.should_be_right_book()
        self.should_be_right_price()
        # assert "9.99" in self.browser.find_element(*ProductPageLocators.PRICE).text, "Price is not correct"

    def should_be_right_book(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return product_price
        


        