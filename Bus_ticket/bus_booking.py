import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BusBooking:
    def __init__(self, driver):
        self.driver = driver
        self.wait  = WebDriverWait(self.driver, 10)
        logging.info("BusBooking class initialized")

    def bus_from(self,city_name):
        logging.info("Clicking on FROM city input")
        self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.inputAndSwapWrapper___7eae05"))).click()

        logging.info(f"Entering FROM city name: {city_name}")
        city_input = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
        city_input.send_keys(city_name)

        logging.info("Waiting for city suggestions")
        city = self.driver.find_elements(By.CSS_SELECTOR, "[class*='searchSuggestionWrapper'] [class*='searchCategory'] [role='option']")
        time.sleep(3)
        for i in city:
            try:
             if i.text == "Delhi":
                self.wait.until(EC.element_to_be_clickable(i))
                break
            except StaleElementReferenceException:
                    continue
        logging.info(" successfully automated")

    def bus_to(self):
        logging.info("Locating TO city input field")
        city_to = self.driver.find_elements(By.CSS_SELECTOR,"div.srcDestWrapper___b2dc42  input ")
        city_to[1].send_keys("var")

        go = self.driver.find_elements(By.CSS_SELECTOR, "div.listItem___765511.lineLength1___aef972.suggestion-item.hoverHighlight___9d49e7")
        for i in go:
            if i.text == "Dehradun":
                logging.info("Dehradun option found, clicking it")
                self.wait.until(EC.element_to_be_clickable(i)).click()
                break
        logging.info("Yes its clicked")

    def date(self):
        logging.info("Opening date picker")
        date_go = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='dateWrapper']")))
        self.driver.execute_script("arguments[0].click();", date_go)
        print(date_go.is_displayed(), date_go.is_enabled())
        date_click = self.driver.find_elements(By.CSS_SELECTOR,"ul.datesWrap___45946c li")
        for i in date_click:
            if i.text == "28":
                logging.info("Selecting travel date: 28")
                self.wait.until(EC.element_to_be_clickable(i)).click()
        logging.info("Date selected successfully")

    def for_women(self):
        logging.info("Clicking on 'Booking for Women' option")
        women_go = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[aria-label='Booking for Women']")))
        women_go.click()

        got = self.wait.until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Got it']")))
        got.click()
        logging.info("'Booking for Women' flow completed")

    def search(self):
        logging.info("Clicking on Search Buses button")
        search_bus = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Search buses']")))
        search_bus.click()
        logging.info("Search bus button clicked successfully")
        time.sleep(2)