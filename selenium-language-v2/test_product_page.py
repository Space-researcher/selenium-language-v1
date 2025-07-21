'''
Run
pytest -v --tb=line --language=en -m need_review .\test_product_page.py
'''
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
import time
import os, random, string   # to generate a password


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Go directly to the registration page;
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        # Creating fake credentials
        template = str(time.time()) + "@fakemail.org"
        email = template[11:]
        length = 10
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        password = ''.join(random.choice(chars) for i in range(length))
        # Output to console for convenience
        print("Credentials: ", email, password)
        # Register a new user;
        self.page.register_new_user(email, password)
        # Checking if the user is logged in (method from bas_page.py)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        # Passing the page to the first test: http://selenium1py.pythonanywhere.com/en-gb/accounts/login/
        # After registration, we are automatically redirected to https://selenium1py.pythonanywhere.com/en-gb/
        # We do not make an order - accordingly, there is no pop-up element
        page.should_not_be_success_message()  # Check if there is a message about successful addition of the product (method from product_page.py)

    # Parameterization disabled
    # test 7 should fail because the book title is "Coders at Work book" instead of "Coders at Work"
    # @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                                   marks=pytest.mark.xfail),
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"])
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_able_by_a_product() # The order methods make_an_order() and solve_quiz_and_get_code() are called.

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_by_a_product()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_empty()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Transition to the login page
    # page.go_to_login_page_invalid_link() # In this case there will be a fail due to the wrong selector
    page.go_to_login_page()
    page.should_be_login_link()
