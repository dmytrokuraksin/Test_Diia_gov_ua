from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def guest_basket(self):
        self.guest_go_to_basket()
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert basket_empty == "Your basket is now empty"