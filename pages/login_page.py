from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_password.send_keys(password)
        confirm_reg_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION)
        confirm_reg_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Incorrect login url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), 'Login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), 'Register form not found'
