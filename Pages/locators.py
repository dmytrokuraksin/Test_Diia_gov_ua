from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, "input.input.form-search_input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn.btn_search-main")
    FOOTER_LIST = (By.CSS_SELECTOR, ".menu_footer > ul :nth-child(1-12)")

class SearchPageLocators:
    pass

class FooterLocators:
    FACEBOOK_FOOTER_BUTTON = (By.CSS_SELECTOR, '.fa-facebook')
    TELEGRAM_FOOTER_BUTTON = (By.CSS_SELECTOR, '.fa-telegram')
    INSTAGRAM_FOOTER_BUTTON = (By.CSS_SELECTOR, '.fa-instagram')
    VIBER_FOOTER_ICON = (By.CSS_SELECTOR, '.fa-viber')




