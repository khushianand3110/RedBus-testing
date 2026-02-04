import logging
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Account:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.click = (By.CSS_SELECTOR,"ul.navOptionsList___f28f95 li")
        self.my_details = (By.CSS_SELECTOR,"div.listItem___765511.lineLength1___aef972")
        self.back = (By.CSS_SELECTOR,"a.errLink")
        self.offer_shows = (By.CSS_SELECTOR,"td.tiles.offerBlock")
        self.cross = (By.CSS_SELECTOR,"i#offerClose")
        self.close = (By.CSS_SELECTOR,"ol.offer-bread-crumb-container li")

    def account_click(self):
        logging.info("Clicking on Account option")
        click = self.driver.find_elements(*self.click)
        for i in click:
            if i.text == "Account":
                i.click()
        logging.info("Account option clicked")

    def bookings(self):
        logging.info("Navigating to Bookings section")
        bookings = self.driver.find_elements(*self.my_details)
        for j in bookings:
            if j.text == "Bookings":
                j.click()
                break

        time.sleep(1)
        logging.info("Navigating to Bookings section")

    def back_home(self):
        logging.info("Clicking back to home link")
        back = self.driver.find_element(*self.back)
        back.click()

    def again_account(self):
        logging.info("Opening Account menu again")
        again = self.driver.find_elements(*self.click)
        for i in again:
            if i.text == "Account":
                i.click()
        time.sleep(2)

    def offers(self):
        logging.info("Opening Account menu again")
        offer_click = self.driver.find_elements(*self.my_details)
        for i in offer_click:
            if i.text == "Offers":
                i.click()
                break

    def in_offers(self):
        logging.info("Selecting an offer from offers list")
        see_offers = self.driver.find_elements(*self.offer_shows)
        see_offers[12].click()

        logging.info("Closing offer popup")
        self.wait.until(EC.element_to_be_clickable(self.cross)).click()
        time.sleep(2)

        logging.info("Scrolling back up to top")
        for i in range(7):
            self.driver.execute_script("window.scrollBy(0,-200);")
        time.sleep(2)

        logging.info("Clicking Home from breadcrumb")
        close_tab = self.driver.find_elements(*self.close)
        for i in close_tab:
            if i.text == "Home":
                i.click()

        time.sleep(3)
        logging.info("Offers flow completed successfully")


