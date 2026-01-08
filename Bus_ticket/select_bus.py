import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selectbus:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.filters = (By.CSS_SELECTOR,"div.filterWrap___a68f38.collapsed___d8d437")
        self.items = (By.CSS_SELECTOR,"div.listItem___c4ae31.lineLength1___3f5d70.hasMetaInfo___cc0477")
        self.provide = (By.CSS_SELECTOR,"div.listItem___c4ae31.lineLength1___3f5d70.hasMetaInfo___cc0477")
        self.view_bus = (By.CSS_SELECTOR,"ul.srpList__ind-search-styles-module-scss-EOdde li")
        self.seats = (By.XPATH,"//span[@tabindex = '-1']")
        self.drop_button = (By.CSS_SELECTOR,"button[aria-label='Select boarding & dropping points'] ")
        self.drop_points = (By.CSS_SELECTOR,"div.bpdpSelection___af2fa2.bpdp")

    def filter_bus(self):
        for _ in range(6):
            self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(1)

        filters = self.driver.find_elements(*self.filters)
        for i in filters:
            if i.text == "Bus type":
                self.wait.until(EC.element_to_be_clickable(i)).click()
        print("Bus type clicked")

    def select_filter(self):
        items = self.driver.find_elements(*self.items)

        required = ["AC", "SLEEPER"]
        for i in items:
            text = i.text
            for r in required:
                if r in text:
                    self.wait.until(EC.element_to_be_clickable(i)).click()

    def filter_2(self):
        for _ in range(5):
            self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(1)

        provide = self.driver.find_elements(*self.filters)
        for i in provide:
            if i.text == "Amenities":
                self.wait.until(EC.element_to_be_clickable(i)).click()

    def select_filter2(self):
        wants = self.driver.find_elements(*self.provide)
        required = ["Blankets", "Charging Point"]
        for j in wants:
            text = j.text
            for r in required:
                if r in text:
                    self.wait.until(EC.element_to_be_clickable(j)).click()
        print("Amenities clicked")

    def click_bus(self):
        for _ in range(2):
            self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(1)

        bus_button = self.driver.find_elements(By.XPATH, "//button[@aria-label = 'View seats for IntrCity SmartBus']")
        bus_button[0].click()
        time.sleep(2)

