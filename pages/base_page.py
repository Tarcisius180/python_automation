from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.clear()  # Clear existing text before entering new text
        element.send_keys(text)

    def verify_attribute(self, locator, expected_text):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected text that contains '{expected_text}' not found in actual text: '{actual_text}'"
        return True

    def verify_page(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL to be '{expected_url}' but was '{actual_url}'"
        return True

    def verify_alert(self, expected_alert_text):
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            if expected_alert_text in alert_text:
                alert.accept()
                return True
            else:
                print(f"Alert text '{alert_text}' does not contain expected text '{expected_alert_text}'")
                return False
        except (TimeoutException, NoAlertPresentException):
            print("No alert present or timeout waiting for alert")
            return False

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.text