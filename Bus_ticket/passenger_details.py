import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Passengerde:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.phone = (By.CSS_SELECTOR,"div.inputBox___5a33dd ")
        self.input=(By.CSS_SELECTOR,"div.inputBox___5a33dd input")
        self.mailbox = (By.CSS_SELECTOR,"input[id='0_5']")
        self.residence = (By.XPATH,"//input[@id='0_201']")
        self.select = (By.CSS_SELECTOR,"div.searchInputWrap___4929b3.undefined input.searchInput___0916b8")
        self.bihar = (By.CSS_SELECTOR,"div.listItem___06cf49 ")
        self.scrolling = (By.CSS_SELECTOR,"div.contentWrap___bc3271")
        self.name_click = (By.CSS_SELECTOR,"input[id='0_4']")
        self.ages = (By.CSS_SELECTOR,"input[id='0_1']")
        self.gender = (By.CSS_SELECTOR,"div.toggleGroup___b983d0.toggleBtn___00a036")
        self.bus_assurance = (By.CSS_SELECTOR,"div.cancellationBreakupWrapper___6d6392")
        self.text = (By.CSS_SELECTOR,"div.cancellationBreakupWrapper___6d6392")
        self.protects = (By.CSS_SELECTOR,"div.insuranceChoice___5421a7")
        self.continuebutton = (By.CSS_SELECTOR,"div.payNowBtn___70bc2c button.primaryButton___3262c2")

    def phone_number(self, number):
        num = self.driver.find_element(*self.phone)
        num.click()
        inputs=self.driver.find_element(*self.input)
        inputs.send_keys(number)
        print("phone number not clicked")

    def mail_id(self):
        box = self.driver.find_element(*self.mailbox)
        box.click()
        box.send_keys("priya123@gmail.com")
        print("mail id was clicked")

    def state(self):
        stateof = self.wait.until(EC.presence_of_element_located(self.residence))
        stateof.click()

        select_state = self.driver.find_element(*self.select)
        select_state.click()
        select_state.send_keys("Bi")

        self.wait.until(EC.element_to_be_clickable(self.bihar)).click()
        print("state clicked")

    def name(self,person):
        scroll=self.driver.find_element(*self.scrolling)
        self.driver.execute_script("arguments[0].scrollIntoView();",scroll)
        print("scrolling")

        option = self.driver.find_element(*self.name_click)
        option.click()
        option.send_keys(person)
        print("option clicked")

    def age(self):
        perage = self.driver.find_element(*self.ages)
        perage.click()
        perage.send_keys("20")
        print("age typed")

    def genderf(self):
        female = self.driver.find_elements(*self.gender)
        for i in female:
            if i.text == "Female":
                i.click()
        print("gender clicked")

    def assurance(self):
        scroll = self.driver.find_element(*self.bus_assurance)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        print("scrolling")

        busassure = self.driver.find_element(*self.text).text
        print(busassure)

    def protect(self):
        protect_trip = self.driver.find_elements(*self.protects)
        for i in protect_trip:
            if i.text == "Yes, protect my trip at ₹ 24 (1 passenger)":
                i.click()
        print("protect clicked")

        self.wait.until(EC.element_to_be_clickable(self.continuebutton)).click()
        time.sleep(5)



