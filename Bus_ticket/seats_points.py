import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeatPoints:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        logging.info("Initializing SeatPoints class and locators")
        self.seats = (By.XPATH, "//span[@aria-pressed = 'false']")
        self.drop_button = (By.CSS_SELECTOR, "button[aria-label='Select boarding & dropping points'] ")
        self.points = (By.CSS_SELECTOR, "div.bpdpSelection___423a9a.bpdp")

    def seat_click(self):
        logging.info("Fetching available seats")
        seat = self.driver.find_elements(*self.seats)
        seat[1].click()
        logging.info("Clicking on seat index 1")
        time.sleep(2)
        logging.info("Seat selected successfully")

    def drop(self):
        logging.info("Clicking boarding & dropping points button")
        drop_points = self.driver.find_element(*self.drop_button)
        drop_points.click()
        logging.info("Boarding & dropping points button clicked")

    def bpoints(self):
        logging.info("Fetching boarding points list")
        bpoint = self.driver.find_elements(*self.points)
        bpoint[3].click()
        logging.info("Boarding point selected successfully")

    def dpoints(self):
        logging.info("Fetching dropping points list")
        dpoint = self.driver.find_elements(*self.points)
        dpoint[6].click()
        logging.info("Dropping point selected successfully")

        time.sleep(3)
        logging.info("SeatPoints flow completed")



