from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class MostActiveStocksPage:

    HEADER = "//h1[@class='Fw(b) Fz(17px) D(ib)']//span"
    STOCK_TABLE = "//table[@class='W(100%)']"

    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 5)
        self.header = wait.until(
            EC.presence_of_element_located((By.XPATH, self.HEADER)))
        self.table_stock = wait.until(
            EC.presence_of_element_located((By.XPATH, self.STOCK_TABLE)))



    def get_header(self):
        return  self.header.text

    def get_stocks_from_table(self):
        self.table_stock