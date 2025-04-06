from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '[id="register_form"]')
    #LOGIN_SUBMIT = (By.CSS_SELECTOR, '[name="login_submit"]')

class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, '[value = "Add to basket"]')
    PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main> p.price_color')
    NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main> h1')
    VIEW_BASKET = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs> span> a')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, 'div.col-sm-1> p')
    NAME_IN_BASKET = (By.CSS_SELECTOR, 'div.col-sm-4> h3> a')
    DIV_1 = (By.CSS_SELECTOR, 'div.alertinner')
    DIV_2 = (By.CSS_SELECTOR, 'div.alert.alert-safe.alert-noicon.alert-info.fade.in> div')
    BOOK = (By.TAG_NAME, 'strong')