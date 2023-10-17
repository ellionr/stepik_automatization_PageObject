from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_items()
        self.should_be_message_of_emptiness()

        pass

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_ITEMS), \
            'There are items in basket'

    def should_be_message_of_emptiness(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            'Message about empty basket not found'
        assert 'Your basket is empty.' in self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
