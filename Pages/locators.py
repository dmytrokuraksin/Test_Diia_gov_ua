from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, "input.input.form-search_input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn.btn_search-main")
    FOOTER_LIST = (By.CSS_SELECTOR, ".menu_footer > ul :nth-child(1-12)")

class SearchPageLocators:
    pass





