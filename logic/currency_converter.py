from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CurrencyConverter:

    CONVERT_BUTTON = "//a[@href='https://www.ofx.com/en-us/yf/?pid=5330' and @class='register-button']"

    TABLE = "//table[@class='widget responsive-layout-landscape']"



    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 7)
        self.table = wait.until(EC.presence_of_element_located((By.XPATH, self.TABLE)))

        self.driver.execute_script("arguments[0].scrollIntoView();", self.table)
        self.convert_button = wait.until(EC.presence_of_element_located((By.XPATH, self.CONVERT_BUTTON)))


    def fill_input_box(self, amount=1):
        self.input_boxself.send_keys(amount)

    def click_convert_button(self):
        self.convert_button.click

    def convert_currency(self, amount=1):
        self.fill_input_box(amount)
        self.click_convert_button()

    def get_input_box(self):
        self.row = self.table.find_elements_by_tag_name("tr")
        self.colume = self.row.find_elements_by_tag_name("td")
        self.colume[0].send_keys("1")

    def enter_input(self, amount):
        self.input_box.send_keys(amount)

    def get_result(self):
        return self.output_box.text
