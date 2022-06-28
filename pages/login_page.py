from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # def should_be_login_page(self):
    #     self.should_be_login_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()

    def should_be_login_url(self):
        #assert "/login" in self.open(), "login is absent in current url"
        #login_url = self.browser.current_url # реализуйте проверку на корректный url адрес
        
        assert "login" in self.browser.current_url, "login is not present in URL"

    def should_be_login_form(self):
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is not presented"
        #assert True

    def should_be_register_form(self):
        register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "Regisret form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        #assert True