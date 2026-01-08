import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Account:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.click = (By.CSS_SELECTOR,"ul.navOptionsList___d533ee li")
        self.my_details = (By.CSS_SELECTOR,"div.listItem___9a15c0.lineLength1___61f928")
        self.back = (By.CSS_SELECTOR,"a.errLink")
        self.offer_shows = (By.CSS_SELECTOR,"td.tiles.offerBlock")
        self.cross = (By.CSS_SELECTOR,"i#offerClose")
        self.close = (By.CSS_SELECTOR,"ol.offer-bread-crumb-container li")

    def account_click(self):
        click = self.driver.find_elements(*self.click)
        for i in click:
            if i.text == "Account":
                i.click()

    def bookings(self):
        bookings = self.driver.find_elements(*self.my_details)
        for j in bookings:
            if j.text == "Bookings":
                j.click()
                break
        time.sleep(1)

    def back_home(self):
        back = self.driver.find_element(*self.back)
        back.click()

    def again_account(self):
        again = self.driver.find_elements(*self.click)
        for i in again:
            if i.text == "Account":
                i.click()
        time.sleep(2)

    def offers(self):
        offer_click = self.driver.find_elements(*self.my_details)
        for i in offer_click:
            if i.text == "Offers":
                i.click()
                break

    def in_offers(self):

        see_offers = self.driver.find_elements(*self.offer_shows)
        see_offers[12].click()

        self.wait.until(EC.element_to_be_clickable(self.cross)).click()
        time.sleep(2)

        for i in range(7):
            self.driver.execute_script("window.scrollBy(0,-200);")
        time.sleep(2)

        close_tab = self.driver.find_elements(*self.close)
        for i in close_tab:
            if i.text == "Home":
                i.click()
        time.sleep(5)



