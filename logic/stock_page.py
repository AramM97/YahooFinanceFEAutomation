from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from YahooFinanceFEAutomation.infra.utils import Utils


class StockPage:
    CLOSE_POPUP_BUTTON = "//button[@class='Bd(0) P(0) D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close' and @aria-label='Close' and @title='Close']"

    HEADER = "//h1[@class='D(ib) Fz(18px)']"

    HISTORICAL_DATA = "//a[contains(@class, 'Lh(44px)')  and @role='tab' and @aria-selected='false']/span[text()='Historical Data']"
    PROFILE = "//a[contains(@class, 'Lh(44px)')  and @role='tab' and @aria-selected='false']/span[text()='Profile']"

    DOWNLOAD_STOCK_HISTORICAL_DATA_BUTTON = "//a[@class='Fl(end) Mt(3px) Cur(p)']"

    ADD_TO_WATCHLIST_BUTTON = "//div[@class='addButton C(white) Bgc($linkSelectedColor) Bgc($linkSelectedHoverColor):h Bdrs(30px) Px(16px) Py(6px)']"

    PROFILE_DESC = "//div[@class='Mb(25px)']"

    ADDED_MESSSAGE = "//p[@class='P(20px) C($checkmarkGreen) Whs(nw) Ell']"

    def __init__(self, driver, stock="NVDA"):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.stock = stock
        self.utils = Utils()

        self.close_popup_button = self.wait.until(EC.presence_of_element_located((By.XPATH, self.CLOSE_POPUP_BUTTON)))
        self.close_popup()

        self.header = self.wait.until(EC.presence_of_element_located((By.XPATH, self.HEADER)))
        self.add_to_watchlist_button = driver.find_element(By.XPATH, self.ADD_TO_WATCHLIST_BUTTON)
        wait = WebDriverWait(driver, 3)
        self.historical_data_section = wait.until(EC.presence_of_element_located((By.XPATH, self.HISTORICAL_DATA)))
        self.profile = wait.until(EC.presence_of_element_located((By.XPATH, self.PROFILE)))



    def close_popup(self):
        self.close_popup_button.click()

    def get_header(self):
        return self.header.text

    def go_to_historical_data(self):
        self.historical_data_section.click()

    def go_to_profile(self):
        self.profile.click()

    def get_stock_desc(self):
        self.stock_desc = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.PROFILE_DESC)))
        return self.stock_desc.text


    def download_stock_historical_data(self):

        self.download_stock_historical_data_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.DOWNLOAD_STOCK_HISTORICAL_DATA_BUTTON)))

        # Get the 'href' attribute
        url = self.download_stock_historical_data_button.get_attribute("href")

        # Print or use the URL as needed
        print("URL:", url)

        self.utils.download_file_main(url, self.stock)

    def add_stock_to_watchlist(self):
        self.add_to_watchlist_button.click()

    def check_added_message(self):
        try:
            self.added_message = self.wait.until(EC.presence_of_element_located((By.XPATH, self.ADDED_MESSSAGE)))
            return True

        except Exception as e:
            print(f"Exception while checking added_message: {e}")
            return False