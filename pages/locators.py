from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1") 
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group .btn-default")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".basket-items .col-sm-4 a")
    PRICE = (By.CSS_SELECTOR, ".col-sm-1 .price_color")
