'''
https://stepik.org/lesson/238819/step/4?auth=login&unit=211271
Файл с тестами
Запуск
 pytest -s .\test_main_page.py::test_guest_cant_see_product_in_basket_negative
'''
from pages.main_page import MainPage
# для перехода на другую страницу - см. main_page.py
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest    # запуск pytest -s -m login_guest .\test_main_page.py
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
       # Медод 1 переход на новую страницу
       #  login_page = page.go_to_login_page()
        # у вызываемого метода был  return LoginPage(browser=self.browser, url=self.browser.current_url)
       #  login_page.should_be_login_page()
        # Медод 2 переход на новую страницу - Инициализируем LoginPage в теле теста
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()   # обращаемся к login_page.py ?

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_empty()  # Это не стал использовать *BasketPageLocators.BASKET_IS_EMPTY

@pytest.mark.xfail(reason="The basket is not empty (known issue)")
def test_guest_cant_see_product_in_basket_negative(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.add_to_basket() # нажать "Купить"
    page.should_be_basket_empty() # тест упадёт
    # по идее, негативный тест должен не находить сообщения и пасаться при этом, вместо xfail.