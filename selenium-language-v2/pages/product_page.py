
'''
4.3 класс Page Object для страницы товара для теста test_product_page.py
файл с проверками
'''

from .locators import ProductPageLocators
from .base_page import BasePage
import time

# Наследование от BasePage
class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_able_by_a_product()
        # self.should_be_name()
        # self.should_be_price()

    # Экспериментальные тесты
    # def should_be_name(self):
    #     assert self.is_element_present(*ProductPageLocators.NAME), "Name is not expected"

    # def should_be_price(self):
    #     assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not expected"


    def should_be_able_by_a_product(self):
        # Читаем имя
        name_element = self.browser.find_element(*ProductPageLocators.NAME)
        name1 = name_element.text
        # Читаем стоимость
        price_element = self.browser.find_element(*ProductPageLocators.PRICE)
        price1 = price_element.text
        time.sleep(5)
        # Жмём кнопку
        button1 = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        button1.click()
        # Рещаем задачу
        self.solve_quiz_and_get_code()

        # Ищем сообщение о добавлении книги в корзину
        # HTML code
        # <div class="alertinner ">
        #     <strong>Coders at Work</strong> has been added to your basket. </div>

        div1 = self.browser.find_element(*ProductPageLocators.DIV_1)
        book = div1.find_element(*ProductPageLocators.BOOK).text
        rest = div1.text.replace(book, '').strip()

        # HTML code
        # <div class="alertinner ">
        # <p> Your basket total is now <strong>£39.97</strong> </p>
        #             </div>

        # div2 = self.browser.find_element(*ProductPageLocators.DIV_2)
        # basket = div2.find_element(By.TAG_NAME, 'strong').text      # потом переделать
        # cost = div2.text.replace(basket, '').strip()

        print(f' Заказ: {book} {rest}')
        # print(f' Корзина: {cost} {basket} ')

        time.sleep(2)
        button2 = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        button2.click()
        time.sleep(2)
        # ждем загрузки корзины
        # поиск цены и названия товара в отдельных методах
        price2 = self.find_price_in_backet()
        name2 = self.find_name_in_backet()
        time.sleep(2)

        # Проверка отображения во сплывающем сообщении
        assert book == name1, "Name is not expected during adding"
        # assert rest == "has been added to your basket.", "Added not correctly"
        # assert basket == "Your basket total is now", "Basket message is not correct"
        # assert cost == price1, "Price is not expected during adding"

        # Проверка отображения в корзине.
        assert name1 == name2, "Name is not expected"
        assert price1 == price2, "Price is not expected"
