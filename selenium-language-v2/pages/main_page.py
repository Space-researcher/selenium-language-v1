'''
файл с проверками
'''
# from .locators import MainPageLocators
from .base_page import BasePage
# для перехода на другую страницу
# from .login_page import LoginPage

class MainPage(BasePage):
    # Заглушка, т.к. все методы (go_to_login_page и should_be_login_link) перенесены в base_page.py
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


    # def go_to_login_page(self):
    #     # Находим кнопку, кликаем, переходим на новую страницу
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()
    #     # Метод 1 - Инициализируем и возвращаем новый объект
    #     # return LoginPage(browser=self.browser, url=self.browser.current_url)
    #     # Метод 2 - Инициализируем LoginPage в теле теста в файле test_main_page.py
    #     # # добавление алерта, если он вдруг появился на странице
    #     # # если алерта нет - будет NoAlertPresentException: Message: no such alert
    #     # alert = self.browser.switch_to.alert
    #     # alert.accept()
    #
    # def should_be_login_link(self):
    #     # символ * это кортеж значений
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"