import time

import pytest
import logging

from pages.login_page import LoginPage



@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_valid_login(self, data_set, logger):
        login_page = LoginPage(self.driver)
        login_data = data_set["test_data"]["valid_login"]
        username = login_data["username"]
        password = login_data["password"]

        logger.info(f"Using valid login with username: {username}")
        login_page.login(username, password)

        time.sleep(3)
        assert login_page.get_logged_in_username() == f"Welcome {username}"
        logger.info("Valid login test passed")

    def test_invalid_login(self, data_set, logger):
        login_page = LoginPage(self.driver)
        login_data = data_set["test_data"]["invalid_login"]
        username = login_data["username"]
        password = login_data["password"]

        try:
            logger.info(f"Using invalid login with username: {username}")
            login_page.login(username, password)

            time.sleep(3)
            assert login_page.verify_account_does_not_exists(), f"Login unsuccessful using {username} and {password}"

        except AssertionError as ae:
            logger.error(f"Assertion error occurred: {str(ae)}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            raise
        finally:
            logger.info("login test completed")

        logger.info("Invalid login test passed")

