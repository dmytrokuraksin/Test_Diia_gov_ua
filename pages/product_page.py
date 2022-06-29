from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.should_be_button_basket()
        self.product_in_basket_is_right()

    def should_be_button_basket(self):

        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def product_in_basket_is_right(self):

        self.should_be_right_book()
        self.should_be_right_price()

    def should_be_right_book(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == name_book, "Name is dismiss"

    def should_be_right_price(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_TOTAL).text
        assert product_price == price_book, "Price is dismiss"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.should_be_button_basket()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
             "Success message is presented, but should not be"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
             "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        self.should_be_button_basket()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
             "Success message is presented, but should not be"
