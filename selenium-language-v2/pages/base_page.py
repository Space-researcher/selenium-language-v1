'''
создание объекта - страницы
'''
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from .locators import ProductPageLocators
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

    # Код для решения задачи во всплывающем окне
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
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
        print(price)
        return price

    def find_name_in_backet(self):
        names = self.browser.find_elements(*ProductPageLocators.NAME_IN_BASKET)
        name = names[0].text
        print(name)
        return name