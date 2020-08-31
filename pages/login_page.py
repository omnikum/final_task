from .base_page import BasePage
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL wrong"

    def should_be_login_form(self):
        assert is_element_present(*MainPageLocators.LOGIN_FORM), "LOGIN FORM IS FUCKED UP"

    def should_be_register_form(self):
        assert is_element_present(*MainPageLocators.REGISTER_FORM), "REGISTER FORM IS FUCKED UP"