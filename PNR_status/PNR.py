import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class PNRstatus:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.check = (By.CSS_SELECTOR,"ul.risContainer___419bc1 li")
        self.enter = (By.CSS_SELECTOR,"div.inputContainer___9737fd")
        self.status = (By.CSS_SELECTOR,"button.primaryButton___3262c2  ")
        self.go_back = (By.XPATH,"//button[normalize-space()='Go Back']")
        self.choose = (By.CSS_SELECTOR,"div.risContainer___a438a5")
        self.type_box = (By.CSS_SELECTOR,"input.pnr-input-text")
        self.train_list = (By.CSS_SELECTOR,"div.lts_solr_wrap")
        self.check_button = (By.CSS_SELECTOR,"button.button.false")

    def check_pnr(self):
        logging.info("Clicking on 'Check PNR status' option")
        check = self.driver.find_elements(*self.check)
        for i in check:
            if i.text == "Check PNR status":
                i.click()
                break
        time.sleep(1)

    def enter_pnr(self,number):
        logging.info("Clicking PNR input container")
        click = self.driver.find_element(*self.enter)
        click.click()

        logging.info(f"Entering PNR number: {number}")
        enter = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME,"input")))
        enter.send_keys(number)
        time.sleep(1)

        status = self.driver.find_element(*self.status)
        status.click()
        time.sleep(1)

        logging.info("PNR status displayed, navigating back")
        back = self.driver.find_element(*self.go_back)
        back.click()
        time.sleep(3)
        logging.info("Returned from PNR status screen")

    def live_status(self,number):
        logging.info("Selecting 'Live train status' option")
        choose_option = self.driver.find_elements(*self.choose)
        for j in choose_option:
            if j.text == "Live train status":
                self.wait.until(EC.element_to_be_clickable(j)).click()
                break

        logging.info("Clicking train number input box")
        type = self.driver.find_element(*self.type_box)
        type.click()

        logging.info(f"Entering train number: {number}")
        enter = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
        enter.send_keys(number)

        lists = self.driver.find_elements(*self.train_list)
        for train in lists:
            try:
                if "12312" in train.text and "Netaji Express" in train.text:
                    logging.info("Matching train found: 12312 Netaji Express")
                    self.wait.until(EC.element_to_be_clickable(train)).click()
                    break
            except StaleElementReferenceException:
                continue
        logging.info("Train selected successfully")

        check = self.driver.find_element(*self.check_button)
        check.click()
        time.sleep(5)
        logging.info("Live train status displayed")





