from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
    
    def send_answer(self):
        self.solve_quiz_and_get_code()
        
        
    def should_be_ok_message(self):
        assert self.is_element_present(*ProductPageLocators.OK_MESSAGE)
        
    
    def should_be_assert_name(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.OK_MESSAGE).text
        
    
    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE)
        
    
    def should_be_assert_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text