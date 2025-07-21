'''
Run single test
 pytest -s .\test_main_page.py::test_guest_cant_see_product_in_basket_negative
Run all tests
 pytest -v --tb=line --language=en .\test_main_page.py
'''
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest    # run  pytest -s -m login_guest .\test_main_page.py
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # Initialize the Page Object, pass the driver instance and URL address to the constructor
        page = MainPage(browser, link)
        page.open()                      
        # Method 1 transition to new page
        #  login_page = page.go_to_login_page()
        # the called method had  return LoginPage(browser=self.browser, url=self.browser.current_url)
        #  login_page.should_be_login_page()
        # Method 2 transition to a new page - Initialize LoginPage in the test body
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
    page.add_to_basket() # Press "Buy"
    page.should_be_basket_empty() # Expected Fail


