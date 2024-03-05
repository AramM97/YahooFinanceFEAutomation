from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CryptoPage:

    HEADER = "//div[@class='D(ib) Fz(m) Fw(b) Lh(23px) W(75%)--mobp']//span//span"

    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 5)
        self.header = wait.until(
            EC.presence_of_element_located((By.XPATH, self.HEADER)))


    def get_header(self):
        return  self.header.text