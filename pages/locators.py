from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, ".register_form button")
    SERVER_ERROR = (By.CSS_SELECTOR, ".jumbotron h1")


class ProductPageLocators:
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1") 
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group .btn-default")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRICE_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")
