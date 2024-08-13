import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUpPage(BasePage):
    # Locators
    SIGNUP_BUTTON = (By.XPATH, '//*[@id="signin2"]')
    USERNAME_FIELD = (By.XPATH, '//*[@id="sign-username"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="sign-password"]')
    FINAL_SIGNUP_BUTTON = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

    def __init__(self, driver):
        super().__init__(driver)

    def open_signup_modal(self):
        self.click_element(self.SIGNUP_BUTTON)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_signup(self):
        self.click_element(self.FINAL_SIGNUP_BUTTON)

    def perform_signup(self, username, password):
        self.open_signup_modal()
        self.enter_username(username)
        self.enter_password(password)
        self.click_signup()

    def verify_signup_successful(self):
        return self.verify_alert("Sign up successful.")

    def verify_account_already_exists(self):
        return self.verify_alert("This user already exist.")