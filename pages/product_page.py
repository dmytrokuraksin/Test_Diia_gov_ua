from .base_page import BasePage


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.should_be_button_basket()
        self.product_in_basket_is_right()
