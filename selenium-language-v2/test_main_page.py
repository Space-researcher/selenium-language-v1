'''
Запуск конкретного теста
 pytest -s .\test_main_page.py::test_guest_cant_see_product_in_basket_negative
Запуск всех тестов
 pytest -v --tb=line --language=en .\test_main_page.py
'''
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest    # запуск pytest -s -m login_guest .\test_main_page.py
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()                      # открываем страницу
        # Медод 1 переход на новую страницу
        #  login_page = page.go_to_login_page()
        # у вызываемого метода был  return LoginPage(browser=self.browser, url=self.browser.current_url)
        #  login_page.should_be_login_page()
        # Медод 2 переход на новую страницу - Инициализируем LoginPage в теле теста
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_empty()

@pytest.mark.xfail(reason="The basket is not empty (known issue)")
def test_guest_cant_see_product_in_basket_negative(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.add_to_basket() # Нажать "Купить"
    page.should_be_basket_empty() # Ожидаемо тест упадёт


