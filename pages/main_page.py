from .base_page import BasePage
from .search_page import SearchPage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_search_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return SearchPage(browser=self.browser, url=self.browser.current_url)

    # def test_guest_can_add_product_to_basket(browser):
    #     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.guest_can_add_product_to_basket()
    #
    # def message_disappeared_after_adding_product_to_basket(self):
    #     self.should_be_button_basket()
    #     assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
    #          "Success message is presented, but should not be"
