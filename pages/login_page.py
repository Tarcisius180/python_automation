from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    # Locators
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login2"]')
    USERNAME_FIELD = (By.XPATH, '//*[@id="loginusername"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="loginpassword"]')
    FINAL_LOGIN_BUTTON = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    LOGGED_IN_USERNAME = (By.XPATH, '//*[@id="nameofuser"]')

    def open_login_modal(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.FINAL_LOGIN_BUTTON)).click()

    def get_logged_in_username(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOGGED_IN_USERNAME)).text

    def login(self, username, password):
        self.open_login_modal()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_account_does_not_exists(self):
        return self.verify_alert("User does not exist.")
