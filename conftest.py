import logging
import os

import pytest
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_file = os.path.join("logs", "my_test.log")
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filemode="a",
    )
    logging.info("========== Test Session Started ==========")

@pytest.fixture

def driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.redbus.in/")
    driver.maximize_window()

    yield driver
    driver.quit()