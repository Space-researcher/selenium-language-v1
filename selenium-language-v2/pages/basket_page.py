
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from .locators import BasketPageLocators
from .base_page import BasePage
import time
import pytest

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_empty()
        self.add_to_basket()

    def add_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET)
        link.click()
        time.sleep(1)

    def should_be_basket_empty(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()
        time.sleep(1)
        try:
            # Тест ждёт появления элемента 10 сек.
            # 1) Можно ожидать так, но это не ускоряет процесс ожидания
            # p_element = WebDriverWait(self.browser, 1).until(lambda d: d.find_element(*BasketPageLocators.BASKET_IS_EMPTY))

            # 2) Можно использовать готовый метод ожидания из base_page.py но в итоге тоже 10 сек ожидания :(
            # возможно, это из-за try-except блока?
            # assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "No message in the basket"

            # Как создать ЕС метод ожидания прямо тут и передавать (how, what) - не стал разбираться
            # WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((how, what)))

            p_element = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
            full_text = p_element.text
            # full_text will be: "Your basket is empty. Continue shopping"
            message = full_text.replace("Continue shopping", "").strip()
            print("Message in the basket: ", message)
            flag = False
            for word in self.languages:
                if message == self.languages[word]:  # сверяемся со значением в словаре языков
                    print("Anything is ok")
                    flag = True
                    break
            assert flag == True, "Seems, basket is not empty"
        except (TimeoutException, NoSuchElementException):
            pytest.fail("Message was not found in the basket or basket is not empty.")






