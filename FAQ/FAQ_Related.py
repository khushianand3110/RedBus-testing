import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Related:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.section = (By.CSS_SELECTOR,"div.sectionTab")
        self.faqitems = (By.CSS_SELECTOR,"div.sectionContent details")
        self.faqanswer = (By.CSS_SELECTOR,"span.faqAnswer p")
        self.popuplar = (By.CSS_SELECTOR,"section.C_155")
        self.type_popular = (By.CSS_SELECTOR,"div.listWrap a")

    def faq_section(self):
        logging.info("Scrolling to FAQ section")
        for i in range(13):
            self.driver.execute_script("window.scrollBy(0,300)")
            time.sleep(1)

        logging.info("Looking for 'Cancellation & Refund' section")
        sections = self.driver.find_elements(*self.section)
        for i in sections:
            if i.text == "Cancellation & Refund":
                i.click()
        logging.info("FAQ section displayed")

    def contents(self):
        logging.info("Searching for FAQ question")
        items = self.driver.find_elements(*self.faqitems)
        for i in items:
            if i.text == "How can I cancel a bus ticket online?":
                self.wait.until(EC.element_to_be_clickable(i)).click()
        logging.info("FAQ question clicked")

    def show_text(self):
        logging.info("Fetching FAQ answer text")
        answer = self.driver.find_elements(*self.faqanswer)
        for i in answer:
            if "cancel the bus ticket online" in i.text:
                print(i.text)
                break
        logging.info("FAQ answer printed in terminal")

    def popular_cities(self):
        logging.info("Scrolling to Popular Cities section")
        for i in range(3):
            self.driver.execute_script("window.scrollBy(0,200)")
            time.sleep(1)

        cities = self.driver.find_elements(*self.popuplar)
        for i in cities:
            if i.text == "Popular Cities":
                self.wait.until(EC.element_to_be_clickable(i)).click()

    def popular_type(self):
        logging.info("Fetching list of popular cities")
        type = self.driver.find_elements(*self.type_popular)
        print(f'all cities are {type}')
        print(len(type))
        for i in type:
            print(i.text)

        time.sleep(3)
        logging.info("Popular cities list displayed")







