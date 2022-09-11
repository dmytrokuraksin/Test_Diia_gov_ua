from .Pages.main_page import MainPage
import pytest
from selenium.webdriver.common.by import By

class TestMainPage():

    def test_guest_can_use_search_form(self, browser):
        link = "https://diia.gov.ua/"
        request = 'реєстрація'
        page = MainPage(browser, link)
        page.open()
        search_page = page.search_info_by_search_form(request)
        search_page.search_result_is_correct()

class TestFooterElementsMainPage():

    @pytest.mark.parametrize('items', [str(x) for x in range(1, 13)])
    def test_footer_list_items_active(self, browser, items):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        footer_element = browser.find_element(By.CSS_SELECTOR, f".menu_footer > ul :nth-child({items})")
        page.footer_list_item_is_active(footer_element)