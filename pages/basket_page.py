from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def guest_basket(self):
        self.guest_go_to_basket()
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
        "Basket is not empty"

    def basket_from_product_page(self):
        self.guest_go_to_basket()
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
        "Basket is not empty"