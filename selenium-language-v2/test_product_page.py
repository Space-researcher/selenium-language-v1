'''
Запуск
pytest -v --tb=line --language=en -m need_review .\test_product_page.py
'''
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
import time
import os, random, string   # для генерации пароля


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Переход сразу на страницу регистрации;
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        # Создание фейковых креденшалов
        template = str(time.time()) + "@fakemail.org"
        email = template[11:]
        length = 10
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        password = ''.join(random.choice(chars) for i in range(length))
        # Вывод в консоль для удобства
        print("Credentials: ", email, password)
        # Зарегистрировать нового пользователя;
        self.page.register_new_user(email, password)
        # Проверка, что пользователь залогинен (метод из bas_page.py)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        # Передаём в первый тест страницу: http://selenium1py.pythonanywhere.com/en-gb/accounts/login/
        # После регистрации автоматически попадаем на https://selenium1py.pythonanywhere.com/en-gb/
        # Заказ не делаем - соответственно, выплывающего элемента нет
        page.should_not_be_success_message()  # Проверяем, есть ли сообщение об успешном добавлении товара (метод из product_page.py)

    # Параметризация отключена
    # тест 7 должен падать из-за названия книги "Coders at Work book" вместо "Coders at Work"
    # @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                                   marks=pytest.mark.xfail),
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"])
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_able_by_a_product() # Вызываются методы заказа make_an_order() и решения задачи solve_quiz_and_get_code()

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
    # Переход на страницу логина
    # page.go_to_login_page_invalid_link() #  В этом случае будет фейл из-за неправильного селектора
    page.go_to_login_page()
    page.should_be_login_link()
