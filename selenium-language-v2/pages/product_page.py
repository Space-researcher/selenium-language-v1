
'''
Class Page Object of the product page for the test test_product_page.py
'''
from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
from .base_page import BasePage
import time

# Inheriting from BasePage
class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_able_by_a_product()

    def should_be_able_by_a_product(self):
        # Different behavior depending on where this check is called from, whether the user is logged in or not
        try:
            # If we are immediately on the book description page
            name_element = self.browser.find_element(*ProductPageLocators.NAME)
            name1 = name_element.text
            price_element = self.browser.find_element(*ProductPageLocators.PRICE)
            price1 = price_element.text
        except NoSuchElementException:
            # If you got to the welcome page after user registration
            button0 = self.browser.find_element(*ProductPageLocators.CHOSE_PROPOSED_BOOK)
            button0.click()
            time.sleep(1)
            name_element = self.browser.find_element(*ProductPageLocators.NAME)
            name1 = name_element.text
            price_element = self.browser.find_element(*ProductPageLocators.PRICE)
            price1 = price_element.text

        time.sleep(5)
        self.make_an_order()    # Making an order (method from base_page.py)
        # self.solve_quiz_and_get_code() # Solve the problem - it is disabled here

        # Looking for a message about adding a book to the cart
        # HTML code
        # <div class="alertinner "> <strong>Coders at Work</strong> has been added to your basket. </div>
        div1 = self.browser.find_element(*ProductPageLocators.DIV_1)
        book = div1.find_element(*ProductPageLocators.BOOK).text
        rest = div1.text.replace(book, '').strip()

        print(f' Заказ: {book} {rest}')
        # View Cart
        time.sleep(2)
        button2 = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        button2.click()
        time.sleep(2)
        # Waiting for the basket to load
        # Search for price and product name in separate methods
        price2 = self.find_price_in_backet()
        name2 = self.find_name_in_backet()
        time.sleep(2)

        # Checking the display in a pop-up message
        assert book == name1, "Name is not expected during adding"

        # Checking the display in the basket.
        assert name1 == name2, "Name is not expected"
        assert price1 == price2, "Price is not expected"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.DIV_1), \
           "Success message is presented, but should not be"

    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.DIV_1), \
           "Success message is presented during 4 sec, but should disappear"
