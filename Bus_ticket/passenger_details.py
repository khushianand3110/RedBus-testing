import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Passengerde:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.phone = (By.CSS_SELECTOR,"div.inputBox___1430ac ")
        self.input=(By.CSS_SELECTOR,"div.inputBox___1430ac input")
        self.mailbox = (By.CSS_SELECTOR,"input[id='0_5']")
        self.residence = (By.XPATH,"//input[@id='0_201']")
        self.select = (By.CSS_SELECTOR,"div.searchInputWrap___cbdabb.undefined input")
        self.bihar = (By.CSS_SELECTOR,"div.listItem___4125f6  ")
        self.scrolling = (By.CSS_SELECTOR,"div.insuranceContent___9efb3b")
        self.name_click = (By.CSS_SELECTOR,"input[id='0_4']")
        self.ages = (By.CSS_SELECTOR,"input[id='0_1']")
        self.gender = (By.CSS_SELECTOR,"div.toggleGroup___cc499d.toggleBtn___d6b642")
        self.bus_assurance = (By.CSS_SELECTOR,"div.insuranceChoice___29f830")
        self.text = (By.CSS_SELECTOR,"div.cancellationBreakupWrapper___1b8ebe span")
        self.protects = (By.CSS_SELECTOR,"div.insuranceChoice___29f830")
        self.continuebutton = (By.CSS_SELECTOR,"div.payNowBtn___755035.undefined  ")

    def phone_number(self, number):
        logging.info("Clicking phone number field")
        num = self.driver.find_element(*self.phone)
        num.click()

        logging.info(f"Entering phone number: {number}")
        inputs=self.driver.find_element(*self.input)
        inputs.send_keys(number)
        logging.info("Phone number entered successfully")

    def mail_id(self):
        logging.info("Clicking email input field")
        box = self.driver.find_element(*self.mailbox)
        box.click()

        box.send_keys("priya123@gmail.com")
        logging.info("Email id entered successfully")

    def state(self):
        logging.info("Selecting state of residence")
        stateof = self.wait.until(EC.presence_of_element_located(self.residence))
        stateof.click()
        time.sleep(3)
        select_state = self.driver.find_element(*self.select)
        select_state.click()
        select_state.send_keys("Bi")
        time.sleep(3)
        logging.info("Selecting Bihar from suggestions")

        self.wait.until(EC.element_to_be_clickable(self.bihar)).click()
        logging.info("State selected successfully")

    def name(self,person):
        logging.info("Scrolling to passenger name section")
        scroll=self.driver.find_element(*self.scrolling)
        self.driver.execute_script("arguments[0].scrollIntoView();",scroll)
        print("scrolling")

        option = self.driver.find_element(*self.name_click)
        option.click()
        option.send_keys(person)
        logging.info("Passenger name entered successfully")

    def age(self):
        logging.info("Entering passenger age")
        perage = self.driver.find_element(*self.ages)
        perage.click()
        perage.send_keys("20")
        logging.info("Passenger age entered successfully")

    def genderf(self):
        logging.info("Selecting gender as Female")
        female = self.driver.find_elements(*self.gender)
        for i in female:
            if i.text == "Female":
                i.click()
        logging.info("Gender selected successfully")

    def assurance(self):
        logging.info("Scrolling to bus assurance section")
        scroll = self.driver.find_element(*self.bus_assurance)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)

        busassure = self.driver.find_element(*self.text).text
        logging.info(f"Bus assurance text captured: {busassure}")

    def protect(self):
        logging.info("Selecting trip protection option")
        protect_trip = self.driver.find_elements(*self.protects)
        for i in protect_trip:
            if i.text == "Yes, protect my trip at ₹ 24 (1 passenger)":
                i.click()
        logging.info("Trip protection selected")

        self.wait.until(EC.element_to_be_clickable(self.continuebutton)).click()
        time.sleep(5)
        logging.info("Continue button clicked successfully")



