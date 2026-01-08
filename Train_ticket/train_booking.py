import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Trainbooking:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_train(self):
        search = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[aria-label='Book trains now to Get ₹100 off using code FESTIVE']")))
        search.click()

        #search = self.driver.find_elements(By.CSS_SELECTOR,"ul.lobList___013e24 li")
        # for i in search:
        #     if i.text == "Train tickets":
        #         self.wait.until(EC.element_to_be_clickable(i)).click()
        #     break
        # time.sleep(4)

