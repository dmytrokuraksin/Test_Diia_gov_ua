from .base_page import BasePage
from .search_page import SearchResultPage
from .locators import MainPageLocators


class MainPage(BasePage):

    def search_info_by_search_form(self, request_data):
        search_input_field = self.browser.find_element(*MainPageLocators.SEARCH_INPUT_FIELD)
        search_input_field.send_keys(request_data)
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
        return SearchResultPage(browser=self.browser, url=self.browser.current_url)

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
