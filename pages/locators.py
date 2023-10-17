from selenium.webdriver.common.by import By


class BasePageLocators:
    LINK_LOGIN = (By.CSS_SELECTOR, '#login_link')
    LINK_BASKET = (By.CSS_SELECTOR, '.basket-mini * a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, '#login_form')
    FORM_REGISTER = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) * strong')
    TOTAL_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) * strong')
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, '#messages .alert-success')


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    LIST_OF_ITEMS = (By.CSS_SELECTOR, '#basket_formset')
