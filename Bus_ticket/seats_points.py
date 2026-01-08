import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeatPoints:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.seats = (By.XPATH, "//span[@aria-pressed = 'false']")
        self.drop_button = (By.CSS_SELECTOR, "button[aria-label='Select boarding & dropping points'] ")
        self.points = (By.CSS_SELECTOR, "div.bpdpSelection___af2fa2.bpdp")
        self.fill_button = (By.CSS_SELECTOR,"button.primaryButton___3262c2.button___2b7236 ")

    def seat_click(self):
        seat = self.driver.find_elements(*self.seats)
        seat[1].click()
        time.sleep(2)

    def drop(self):
        drop_points = self.driver.find_element(*self.drop_button)
        drop_points.click()
        print("button clicked")

    def bpoints(self):
        bpoint = self.driver.find_elements(*self.points)
        bpoint[1].click()
        print("board Points clicked")

    def dpoints(self):
        dpoint = self.driver.find_elements(*self.points)
        dpoint[5].click()
        print("drop points clicked")

