import json
import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Create logs directory if it doesn't exist
LOGS_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Setup logging
@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    log_file = os.path.join(LOGS_DIR, 'test_log.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

@pytest.fixture(scope="class")
def config_data():
    try:
        with open("../config.json") as config_file:
            data = json.load(config_file)
            return data
    except FileNotFoundError:
        print("Couldn't find the config file")
        raise

@pytest.fixture(scope="class")
def data_set():
    try:
        with open("../test_data.json") as config_file:
            data = json.load(config_file)
            return data
    except FileNotFoundError:
        print("Couldn't find the config file")
        raise

@pytest.fixture(scope="function")
def driver(request, config_data, logger):
    browser = config_data["browser"]
    headless = config_data["headless"]
    implicitwait = config_data["implicit"]
    url = config_data["url"]

    logger.info(f"Initializing {browser} browser")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(implicitwait)
    driver.get(url)
    logger.info(f"Navigating to URL: {url}")

    request.cls.driver = driver
    yield
    logger.info("Closing browser")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

# Hook for taking screenshot on test failure
import os
from datetime import datetime
import pytest

# Relative path for screenshots
SCREENSHOT_PATH = os.path.join(os.path.dirname(__file__), "..", "screenshots")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.instance.driver
        take_screenshot(driver, item.name)

def take_screenshot(driver, name):
    if not os.path.exists(SCREENSHOT_PATH):
        os.makedirs(SCREENSHOT_PATH)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join(SCREENSHOT_PATH, screenshot_name)
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")