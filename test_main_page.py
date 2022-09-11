from .pages.main_page import MainPage

def test_guest_cant_use_searh_form(browser):
    link = "https://diia.gov.ua/"
    request = 'реєстрація'
    page = MainPage(browser, link)
    page.open()
    search_page = page.search_info_by_search_form(request)
    search_page.search_result_is_correct(request)
