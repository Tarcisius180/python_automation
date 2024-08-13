from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locators
    PHONE_CATEGORY_BUTTON = (By.XPATH, '//*[@id="itemc"]')
    ADD_ITEM = (By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
    ADD_TO_CART = (By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
    CART_BUTTON = (By.XPATH, '//*[@id="cartur"]')
    MAKE_ORDER = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
    ENTER_NAME = (By.XPATH, '//*[@id="name"]')
    ENTER_COUNTRY = (By.XPATH, '//*[@id="country"]')
    ENTER_STATE = (By.XPATH, '//*[@id="city"]')
    ENTER_CARD = (By.XPATH, '//*[@id="card"]')
    ENTER_MONTH = (By.XPATH, '//*[@id="month"]')
    ENTER_YEAR = (By.XPATH, '//*[@id="year"]')
    CLICK_SUBMIT = (By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
    ORDER_CONFIRMATION = (By.XPATH, '/html/body/div[10]/p')

    def __init__(self, driver):
        super().__init__(driver)

    def select_phone_category(self):
        self.click_element(self.PHONE_CATEGORY_BUTTON)

    def add_item_to_cart(self):
        self.click_element(self.ADD_ITEM)
        self.click_element(self.ADD_TO_CART)

    def go_to_cart(self):
        self.click_element(self.CART_BUTTON)

    def place_order(self, name, country, state, card, month, year):
        self.click_element(self.MAKE_ORDER)
        self.enter_text(self.ENTER_NAME, name)
        self.enter_text(self.ENTER_COUNTRY, country)
        self.enter_text(self.ENTER_STATE, state)
        self.enter_text(self.ENTER_CARD, card)
        self.enter_text(self.ENTER_MONTH, month)
        self.enter_text(self.ENTER_YEAR, year)
        self.click_element(self.CLICK_SUBMIT)

    def get_order_confirmation(self):
        return self.get_element_text(self.ORDER_CONFIRMATION)

    def extract_order_id(self, confirmation_text):
        lines = confirmation_text.split("\n")
        id_line = next((line for line in lines if line.startswith("Id:")), None)
        if id_line:
            return id_line.split(":")[1].strip()
        return None