'''
https://stepik.org/lesson/238819/step/4?auth=login&unit=211271
Файл с тестами
'''
from pages.main_page import MainPage
# для перехода на другую страницу - см. main_page.py
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
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

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

