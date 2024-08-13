import time
import pytest
from pages.signUp_Page import SignUpPage


@pytest.mark.usefixtures("driver")
class TestSignUp:
    def test_signup(self, data_set, logger):
        signup_page = SignUpPage(self.driver)
        sign_up_data = data_set["test_data"]["valid_sign_up"]
        username = sign_up_data["username"]
        password = sign_up_data["password"]

        logger.info(f"Attempting sign up with username: {username}")
        time.sleep(3)
        signup_page.perform_signup(username, password)

        if signup_page.verify_account_already_exists():
            logger.error(f"Account with username {username} already exists.")
            pytest.fail(f"Test failed: There is an account already with username {username}")
        else:
            assert signup_page.verify_signup_successful(), f"Sign up for user {username} was not successful"
            logger.info(f"Successfully signed up with username: {username}")
