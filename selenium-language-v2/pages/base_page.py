'''
создание объекта - страницы
'''
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException  # в начале файла

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

    #  4.3 Улучшаем дизайн тестов 8 out of 15 steps
    # Методы переходов на страницы логинов - универсальные
    def go_to_login_page_invalid_link(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    #  4.3 Улучшаем дизайн тестов 5 out of 15 steps Отрицательные проверки
    def is_not_element_present(self, how, what, timeout=4):
        # Открываем страницу, заказ НЕ делаем, и проверяем, есть ли всплывающий элемент
        # Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        # Делаем заказ, находим элемент
        # тест будет ждать 4 сек, пока элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def make_an_order(self):
        # Жмём кнопку
        button1 = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        button1.click()

    # Код для решения задачи во всплывающем окне
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)   # решаем задачу, вводим решение
        alert.accept()
        try:
            alert = self.browser.switch_to.alert   # получаем второй алерт с ответом
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Методы для поиска цены и имени в корзине
    def find_price_in_backet(self):
        # ищем новые элементы для проверки - в корзине несколько книг, выбираем первую
        prices = self.browser.find_elements(*ProductPageLocators.PRICE_IN_BASKET)
        price = prices[0].text
        print("Цена в корзине = ", price)
        return price

    def find_name_in_backet(self):
        names = self.browser.find_elements(*ProductPageLocators.NAME_IN_BASKET)
        name = names[0].text
        print("Имя в корзине = ", name)
        return name

    # Метод для финального задания 4.3
    # Если пользователь зарегистрирован - появляется кнопка Logout
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_LOGOUT), "User icon is not presented," \
                                                                     " probably unauthorised user"
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