from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # USER_ICON = (By.CSS_SELECTOR, ".icon-user")   # При регистрации не находит этой иконки :(
    USER_LOGOUT = (By.CSS_SELECTOR, '[id="logout_link"]')

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs> span> a")
    BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[data-loading-text="Adding..."]')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '[id="register_form"]')
    REGISTERATION_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTERATION_PWD1 = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTERATION_PWD2 = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTERATION_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')

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
    CHOSE_PROPOSED_BOOK = (By.CSS_SELECTOR, 'div.row> div.col-sm-9> h3> a')
