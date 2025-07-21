'''
Creating an object - page
'''
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import BasketPageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Methods for transitions to login pages are universal
    def go_to_login_page_invalid_link(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    #  Negative checks
    def is_not_element_present(self, how, what, timeout=4):
        # Open the page, do NOT make an order, and check if there is a pop-up element
        # Will fall as soon as it sees the element it is looking for. Didn't appear: success, test is green.
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        # Make an order, find an element
        # The test will wait 4 seconds until the element disappears.
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def make_an_order(self):
        button1 = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        button1.click()

    # Code to solve the problem in the pop-up window
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)   # Solve the problem, enter the solution
        alert.accept()
        try:
            alert = self.browser.switch_to.alert   # Receive a second alert with a response
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Methods for finding price and name in cart
    def find_price_in_backet(self):
        # We are looking for new items to check - there are several books in the basket, we select the first one
        prices = self.browser.find_elements(*ProductPageLocators.PRICE_IN_BASKET)
        price = prices[0].text
        print("Price in cart = ", price)
        return price

    def find_name_in_backet(self):
        names = self.browser.find_elements(*ProductPageLocators.NAME_IN_BASKET)
        name = names[0].text
        print("Name in cart = ", name)
        return name

    # Checking that if the user is registered, the Logout button appears
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_LOGOUT), "User icon is not presented," \
                                                                     " probably unauthorised user"
    # Messages about the availability of goods in the basket in different languages
    languages = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "en-gb": "Your basket is empty.",
        "en-US": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }
