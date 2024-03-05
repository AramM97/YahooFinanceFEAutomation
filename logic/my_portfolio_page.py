import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from YahooFinanceFEAutomation.infra.utils import Utils

class MyPortfolioPage:

    CREATE_PORTFOLIO_BUTTON = "//button[@data-test='create-pf-btn']"

    PORTFOLIO_BUTTON = "//button[@data-test='next']"
    PORTFOLIO_NAME_INPUT = "//input[@data-test='input-beta-pf-name']"
    PORTFOLIO_CREATE_BUTTON = "//button[@data-test='createPfBeta']"

    HEADER = "//h1[@class='Fw(b) Fz(17px) D(ib)']"

    ADD_SYMBOL = "//div[@data-test='add-symbol-btn']//span"
    ADD_SYMBOL2 = "//span[text()='Add Symbol']"

    MY_STOCK = "//a[@data-test='quoteLink']"

    SEARCH_SYMBOL = "//input[@class='Bdrs(0) Bxsh(n)! Fz(s) Bxz(bb) D(ib) Bg(n) Px(30px) Py(0) H(30px) Lh(30px) Bd O(n):f O(n):h Bdc($seperatorColor) Bdc($linkColor):f Bdc($breakingRed):inv C($negativeColor):inv Pend(30px) W(100%)  finsrch-inpt']"

    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 3)
        self.create_portfolio_button = wait.until(EC.presence_of_element_located((By.XPATH, self.CREATE_PORTFOLIO_BUTTON)))
        self.header = wait.until(EC.presence_of_element_located((By.XPATH, self.HEADER)))
        self.utils = Utils()

    def get_header(self):
        return self.header.text

    def create_portfolio(self, pf_name="Portfolio_test"):
        pf_name = self.utils.get_random_pf_name(6)
        self.create_portfolio_button.click()
        self.wait = WebDriverWait(self.driver, 3)
        self.protfolio_button_next = self.wait.until(EC.presence_of_element_located((By.XPATH, self.PORTFOLIO_BUTTON)))
        self.protfolio_button_next.click()
        self.protfolio_name_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.PORTFOLIO_NAME_INPUT)))
        self.protfolio_name_input.send_keys(pf_name)
        self.protfolio_create_button = self.wait.until(EC.presence_of_element_located((By.XPATH, self.PORTFOLIO_CREATE_BUTTON)))
        self.protfolio_create_button.click()

    def click_add_symbol(self):
        try:
            print("Clicking add symbol...")
            self.add_symbol = self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.ADD_SYMBOL2)))
            self.add_symbol.click()
        except StaleElementReferenceException:
            print("Clicking add symbol...")
            self.add_symbol = self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.ADD_SYMBOL2)))
            self.add_symbol.click()

    def add_stock(self, symbol):
        self.click_add_symbol()


        time.sleep(2)

        # Add an explicit wait after clicking "Add Symbol"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_SYMBOL)))

        print("Typing symbol to search...")
        self.search_symbol = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_SYMBOL)))
        self.search_symbol.send_keys(symbol)
        self.search_symbol.send_keys(Keys.RETURN)
        print("Symbol added successfully.")

    def add_random_symbols(self):
        stocks = self.utils.choose_random_stocks("portfolio.json", num_stocks=1)
        for stock in stocks:
            self.add_stock(stock)

    def check_added_Stock(self):
        self.my_stock = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.MY_STOCK)))
        return self.my_stock.text





