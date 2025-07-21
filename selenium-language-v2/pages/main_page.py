
# from .locators import MainPageLocators
from .base_page import BasePage
# to go to another page
# from .login_page import LoginPage

class MainPage(BasePage):
    # Stub, because all methods (go_to_login_page and should_be_login_link) have been moved to base_page.py
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()
    #
    # def should_be_login_link(self):
    #     # the symbol * is a tuple of values
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
