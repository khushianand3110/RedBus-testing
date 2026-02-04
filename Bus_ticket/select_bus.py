import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selectbus:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.filters = (By.CSS_SELECTOR,"div.filterWrap___5a3359.collapsed___c4ff82")
        self.items = (By.CSS_SELECTOR,"div.swipeWrapper___c64948")
        self.provide = (By.CSS_SELECTOR,"div.swipeWrapper___c64948")
        self.view_bus = (By.CSS_SELECTOR,"ul.srpList__ind-search-styles-module-scss-EOdde li")
        self.seats = (By.XPATH,"//span[@tabindex = '-1']")
        self.drop_button = (By.CSS_SELECTOR,"button[aria-label='Select boarding & dropping points'] ")
        self.drop_points = (By.CSS_SELECTOR,"div.bpdpSelection___af2fa2.bpdp")
        self.select_bus = (By.XPATH, "//button[@aria-label = 'View seats for IntrCity SmartBus']")

    def filter_bus(self):
        logging.info("Scrolling to load bus type filter")
        for _ in range(6):
            self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(1)

        filters = self.driver.find_elements(*self.filters)
        for i in filters:
            if i.text == "Bus type":
                logging.info("Clicking Bus type filter")
                self.wait.until(EC.element_to_be_clickable(i)).click()
        logging.info("Bus type filter applied")

    def select_filter(self):
        logging.info("Selecting bus type filters (AC, SLEEPER)")
        items = self.driver.find_elements(*self.items)

        required = ["AC", "SLEEPER"]
        for i in items:
            text = i.text
            for r in required:
                if r in text:
                    self.wait.until(EC.element_to_be_clickable(i)).click()
        logging.info("Bus type options selected")

    def filter_2(self):
        logging.info("Scrolling to load Amenities filter")
        for _ in range(5):
            self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(1)

        provide = self.driver.find_elements(*self.filters)
        for i in provide:
            if i.text == "Amenities":
                logging.info("Clicking Amenities filter")
                self.wait.until(EC.element_to_be_clickable(i)).click()
        logging.info("Amenities filter opened")

    def select_filter2(self):
        logging.info("Selecting Amenities options (Blankets, Charging Point)")
        wants = self.driver.find_elements(*self.provide)
        required = ["Blankets", "Charging Point"]
        for j in wants:
            text = j.text
            for r in required:
                if r in text:
                    self.wait.until(EC.element_to_be_clickable(j)).click()
        logging.info("Amenities selected successfully")

    def click_bus(self):
        logging.info("Scrolling to view available buses")
        for _ in range(2):
            self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(1)

        bus_button = self.driver.find_elements(*self.select_bus)
        bus_button[0].click()
        time.sleep(2)
        logging.info("Bus selected and seats view opened")

