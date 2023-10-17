import math

from selenium.common import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_added_to_basket(self):
        self.should_be_message_about_adding_product()
        self.should_be_message_with_total_price()

    def should_be_message_about_adding_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), \
            "Message about adding product to the basket not found"

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, \
            "Product name on the message does not match the product you added"

    def should_be_message_with_total_price(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE), \
            "Message with total price not found"

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        assert product_price == total_price, "Total price does not match the product price"

    def should_not_be_success_message_present(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS)

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
