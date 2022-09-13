import time

from .base_page import BasePage
from .search_page import SearchResultPage
from .locators import MainPageLocators
from .locators import FooterLocators


class MainPage(BasePage):

    def search_info_by_search_form(self, request_data):
        search_input_field = self.browser.find_element(*MainPageLocators.SEARCH_INPUT_FIELD)
        search_input_field.send_keys(request_data)
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
        return SearchResultPage(browser=self.browser, url=self.browser.current_url)

    def footer_list_item_is_active(self, item):
        assert item != None

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

    def footer_telegram_button_work_correct(self):
        telegram_button = self.browser.find_element(*FooterLocators.TELEGRAM_FOOTER_BUTTON)
        telegram_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 't.me' in link, 'Telegram button works incorrect!'

    def footer_facebook_button_work_correct(self):
        facebook_button = self.browser.find_element(*FooterLocators.FACEBOOK_FOOTER_BUTTON)
        facebook_button.click()
        time.sleep(5)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(10)
        link = self.browser.current_url
        assert 'facebook' in link, 'Facebook button works incorrect!'

    def footer_instagram_button_work_correct(self):
        instagram_button = self.browser.find_element(*FooterLocators.INSTAGRAM_FOOTER_BUTTON)
        instagram_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'instagram' in link, 'Instagram button works incorrect!'

    def footer_viber_button_work_correct(self):
        viber_button = self.browser.find_element(*FooterLocators.VIBER_FOOTER_ICON)
        viber_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'viber' in link, 'Viber button works incorrect!'

    def footer_app_store_button_work_correct(self):
        viber_button = self.browser.find_element(*FooterLocators.APP_STORE_FOOTER_BUTTON)
        viber_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'apps.apple.com' in link, 'App store button works incorrect!'

    def footer_google_play_market_button_work_correct(self):
        viber_button = self.browser.find_element(*FooterLocators.GOOGLE_PLAY_FOOTER_BUTTON)
        viber_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'play.google.com' in link, 'Google play button works incorrect!'

    def footer_app_gallery_button_work_correct(self):
        viber_button = self.browser.find_element(*FooterLocators.APP_GALLERY_FOOTER_BUTTON)
        viber_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'appgallery.huawei.com' in link, 'App gallery button works incorrect!'
