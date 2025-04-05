'''
файл с проверками
'''

from .locators import LoginPageLocators
from .base_page import BasePage

# Наследование от BasePage
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # https://stepik.org/lesson/36285/step/9?unit=162401
        # новый линк для раздела  4.2, 8 out of 12 steps
        assert "login" in self.browser.current_url, "Открылась не та страница, login отсутствует"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # assert True
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # assert True
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

