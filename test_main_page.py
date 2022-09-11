import time

from .Pages.main_page import MainPage


class TestMainPage():
    def test_guest_can_use_search_form(self, browser):
        link = "https://diia.gov.ua/"
        request = 'реєстрація'
        page = MainPage(browser, link)
        page.open()
        search_page = page.search_info_by_search_form(request)
        time.sleep(10)
        search_page.search_result_is_correct(request)