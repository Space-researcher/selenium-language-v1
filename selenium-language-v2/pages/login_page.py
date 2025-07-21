'''
File with checks
'''

from .locators import LoginPageLocators
from .base_page import BasePage

# Inheriting from BasePage
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        #self.register_new_user()  # It works without this and doesn't complain about missing parameters.

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "The wrong page opened, login is missing"

    def should_be_login_form(self):
        # implement a check that there is a login form
        # assert True
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # implement a check that there is a registration form on the page
        # assert True
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # takes two strings and logs the user in. Implement it by describing the appropriate page elements.

        r1 = self.browser.find_element(*LoginPageLocators.REGISTERATION_EMAIL)   # find_element но НЕ find_elementS
        r1.send_keys(email)
        r2 = self.browser.find_element(*LoginPageLocators.REGISTERATION_PWD1)
        r2.send_keys(password)
        r3 = self.browser.find_element(*LoginPageLocators.REGISTERATION_PWD2)
        r3.send_keys(password)
        rbtn = self.browser.find_element(*LoginPageLocators.REGISTERATION_BTN)
        rbtn.click()


