'''
Lesson link
https://stepik.org/lesson/238819/step/8?auth=login&unit=211271
'''
from pages.login_page import LoginPage


def test_can_open_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_guest_login(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)   # initialize Page Object, pass the driver instance and URL address to the constructor
    page.open()                      
    page.should_be_login_form()       

def test_guest_can_register(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
