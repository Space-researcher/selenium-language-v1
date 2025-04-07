'''
4.3  новый файл для тест-кейсов, связанных со страницей товара.
запуск
pytest -s .\test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page
'''
from pages.login_page import LoginPage
from pages.product_page import ProductPage
#from pages.product_page import ProductFactory
#from pages.basket_page import BasketPage
import pytest
import time
import os, random, string   # для генерации пароля


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # переход сразу на страницу регистрации;
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        # Создание фейковых креденшалов
        email = str(time.time()) + "@fakemail.org"
        length = 10
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        password = ''.join(random.choice(chars) for i in range(length))

        print("Credentials: ", email, password)
        self.page.register_new_user(email, password)   # тут тест ломается
        # зарегистрировать нового пользователя;
        self.page.should_be_authorized_user()  # проверка пользователь залогинен из bas_page.py

    def test_user_cant_see_success_message(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, self.link)
        page.open()
        print("Передаём страницу в первый тест: ",  self.link)   # http://selenium1py.pythonanywhere.com/en-gb/accounts/login/
        # На самом деле после регистрации попадаем автоматом на https://selenium1py.pythonanywhere.com/en-gb/
        # Заказ не делаем - соответственно, выплывающего элемента нет
        page.should_not_be_success_message()  # Проверяем, есть ли сообщение об успешном добавлении товара product_page.py


    # Параметризация отключена
    # offer7 должен падать из-за названия книги "Coders at Work book" вместо "Coders at Work"
    # @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                                   pytest.param(
    #                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                                       marks=pytest.mark.xfail),
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_basket(self, browser):
        # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_able_by_a_product()
        # Методы заказа make_an_order() и решения задачи solve_quiz_and_get_code() вызываются изнутри


# @pytest.mark.login                 # запуск pytest -s -m login .\test_product_page.py
# class TestLoginFromProductPage():
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self):
#         self.product = ProductFactory(title="Best book created by robot")   # такой книги нет :(
#         # создаем по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали
#         self.product.delete()
#
#     def test_guest_should_see_login_link_on_product_page(self, browser):
#         #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
#         page = ProductPage(browser, self.link)
#         page.open()
#         page.should_be_login_link()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#         page = ProductPage(browser, self.link)
#         page.open()
#         # Переход на страницу логина
#         # page.go_to_login_page_invalid_link() #  будет фейл из-за неправильного селектора
#         page.go_to_login_page()
#         page.should_be_login_link()
#
#
#
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = BasketPage(browser, link)
#     page.open()
#     page.should_be_basket_empty()
#
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.make_an_order()  # Делаем заказ
#     page.should_not_be_success_message()  # Тест падает
#
# # Тест на проверку исчезающих элементов должен ПАДАТЬ т.к. никакие элементы здесь не исчезают
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.make_an_order()  # Делаем заказ
#     page.solve_quiz_and_get_code()  # Решаем задачу
#     page.should_disappear_message()  #  Проверяем, что сообщение о добавлении товара пропадает


# def test_can_read_name(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_name()
#
# def test_can_read_price(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_price()

