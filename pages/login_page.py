from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def register_new_user(self):

        email = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("fffFFF123.")
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        password.send_keys("fffFFF123.")
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not present in URL"

    def should_be_login_form(self):
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is not presented"

    def should_be_register_form(self):
        register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "Register form is not presented"
