from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest


# @pytest.mark.login_guest
# class TestLoginFromMainPage():

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_basket()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
def test_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
     # page = page.go_to_login_page()
    page.go_to_login_page()        # выполняем метод страницы — переходим на страницу логина
# def test_should_be_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
#     page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_be_login_url()          # выполняем метод страницы — переходим на страницу логина

# def test_should_be_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
#     page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_be_login_form()
#
# def test_should_be_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
#     page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_be_register_form()