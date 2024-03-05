from selenium.common import StaleElementReferenceException
from selenium.common import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class HomePage:
    SIGN_IN_BUTTON = "//a[@id='header-signin-link' and contains(@class, 'Bgc(#fff)') and contains(@href, 'https://login.yahoo.com')]"


    MY_PORTFOLIO = "//a[@title='My Portfolio']"
    CRYPTO = "//a[@title='Crypto']"
    MARKETS_TAB = "//a[@title='Markets']"

    CURRENCY_CONVERTER = "//a[@title='Currency Converter']"

    MOST_ACTIVE_STOCKS = "//a[@title='Stocks: Most Actives']"

    SEARCH_FIELD = "//input[@id='yfin-usr-qry']"

    USER_PROFILE = "//button[@id='header-profile-button']"

    def __init__(self, driver):
        self.driver = driver
        self.my_portfolio = driver.find_element(By.XPATH, self.MY_PORTFOLIO)
        self.markets = driver.find_element(By.XPATH, self.MARKETS_TAB)
        self.sign_in_button = driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
        self.search_field = driver.find_element(By.XPATH, self.SEARCH_FIELD)
        self.crypto = driver.find_element(By.XPATH, self.CRYPTO)

    def go_to_portfolio(self):
        try:
            my_portfolio = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.MY_PORTFOLIO)))
            my_portfolio.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            my_portfolio = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.MY_PORTFOLIO)))
            my_portfolio.click()

    def sign_in_button_click(self):
        self.sign_in_button.click()

    def search_for_stock(self, stock):
        self.search_field.send_keys(stock)
        self.search_field.send_keys(Keys.RETURN)

    def hover_markets_tab(self):
        # Create an ActionChains object
        actions = ActionChains(self.driver)
        # Perform the hover over action
        actions.move_to_element(self.markets).perform()


    def go_to_currency_converter(self):
        self.currency_converter_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.CURRENCY_CONVERTER)))
        self.currency_converter_tab.click()

    def go_to_most_active_stocks(self):
        self.most_active_tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.MOST_ACTIVE_STOCKS)))
        self.most_active_tab.click()

    def go_to_crypto(self):
        self.crypto.click()

    def get_user_profile(self):
        try:
            user_profile = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.USER_PROFILE)))
            return True
        except ElementNotVisibleException:
            return False






    