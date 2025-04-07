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
        #self.register_new_user()  # Работает и без этого, не ругается на недостающие параметры

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

    def register_new_user(self, email, password):
        # принимает две строки и регистрирует пользователя. Реализуйте его, описав соответствующие элементы страницы.

        r1 = self.browser.find_element(*LoginPageLocators.REGISTERATION_EMAIL)   # find_element но НЕ find_elementS
        r1.send_keys(email)
        r2 = self.browser.find_element(*LoginPageLocators.REGISTERATION_PWD1)
        r2.send_keys(password)
        r3 = self.browser.find_element(*LoginPageLocators.REGISTERATION_PWD2)
        r3.send_keys(password)
        rbtn = self.browser.find_element(*LoginPageLocators.REGISTERATION_BTN)
        rbtn.click()


