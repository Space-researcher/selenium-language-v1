'''
Задание:
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
Тест должен запускаться с параметром language следующей командой:  pytest --language=es test_items.py
Достаточно, чтобы код работал только для браузера Сhrome.
'''

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_basket_is_present_on_the_page(browser):
    browser.get(link)
    try:
        button = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.add-to-basket > button'))
        )
        assert button.is_displayed(), "Add to basket button is not visible"
    except (NoSuchElementException, TimeoutException):
        assert False, "Add to basket button was not found on the page"