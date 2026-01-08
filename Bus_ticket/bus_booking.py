import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException



class BusBooking:
    def __init__(self, driver):
        self.driver = driver
        self.wait  = WebDriverWait(self.driver, 10)

    def bus_from(self,city_name):
        self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.inputAndSwapWrapper___ed8f88"))).click()

        city_input = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
        city_input.send_keys(city_name)

        city = self.driver.find_elements(By.CSS_SELECTOR, "[class*='searchSuggestionWrapper'] [class*='searchCategory'] [role='option']")
        for i in city:
            try:
             if i.text == "Delhi":
                i.click()
                break
            except StaleElementReferenceException:
                continue

    def bus_to(self):
        city_to = self.driver.find_elements(By.CSS_SELECTOR,"input.inputField___862dea")
        city_to[1].send_keys("var")

        go = self.driver.find_elements(By.CSS_SELECTOR, "div.listItem___9a15c0.lineLength1___61f928.suggestion-item.hoverHighlight___dda210 ")
        for i in go:
            if i.text == "Dehradun":
                self.wait.until(EC.element_to_be_clickable(i)).click()
                break
        print("yes its clicked")

    def date(self):
        date_go = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='dateWrapper']")))
        self.driver.execute_script("arguments[0].click();", date_go)
        print(date_go.is_displayed(), date_go.is_enabled())
        date_click = self.driver.find_elements(By.CSS_SELECTOR,"ul.datesWrap___add8bb li")
        for i in date_click:
            if i.text == "31":
                self.wait.until(EC.element_to_be_clickable(i)).click()
        print("Date clicked")

    def for_women(self):
        women_go = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"label.switchLabel___a8ead2.unChecked___09ee04.enabled___ad293b")))
        women_go.click()

        got = self.wait.until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Got it']")))
        got.click()

    def search(self):
        search_bus = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Search buses']")))
        search_bus.click()
        print("Search bus clicked")
        time.sleep(2)