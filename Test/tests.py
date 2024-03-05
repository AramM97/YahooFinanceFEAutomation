import unittest

from YahooFinanceFEAutomation.logic.home_page import HomePage
from YahooFinanceFEAutomation.logic.sign_in_page import SignInPage
from YahooFinanceFEAutomation.logic.stock_page import StockPage
from YahooFinanceFEAutomation.logic.my_portfolio_page import MyPortfolioPage
from YahooFinanceFEAutomation.logic.most_active_stocks_page import MostActiveStocksPage
from YahooFinanceFEAutomation.logic.crypto_page import CryptoPage




class tests(unittest.TestCase):

    def test_go_to_portfolio(self):
        driver = self.browser.get_driver()
        self.homepage = HomePage(driver)
        self.homepage.go_to_portfolio()
        self.my_protfolio_page = MyPortfolioPage(driver)
        header = self.my_protfolio_page.get_header()

        #assert
        self.assertIn(header, "My Portfolios", "Wrong Page")


    def test_sign_in(self):
        driver = self.browser.get_driver()

        self.homepage = HomePage(driver)
        self.homepage.sign_in_button_click()
        self.signin_page = SignInPage(driver)
        self.signin_page.signin_flow()

        is_signed = self.homepage.get_user_profile()

        #assert
        self.assertTrue(is_signed, "user not signed")


    def test_portfolio(self, driver):
        #driver = self.browser.get_driver()
        self.homepage = HomePage(driver)

        # signin process
        self.homepage.sign_in_button_click()
        self.signin_page = SignInPage(driver)
        self.signin_page.signin_flow()

        self.homepage.go_to_portfolio()
        self.my_protfolio_page = MyPortfolioPage(driver)

        self.my_protfolio_page.create_portfolio()
        self.my_protfolio_page.add_random_symbols()
        #self.my_protfolio_page.add_symbol("TSLA")
        added_stock = self.my_protfolio_page.check_added_Stock()

        self.assertIsNotNone(added_stock,"Stock Not Added")



    def test_search_for_stock(self, driver):
        self.homepage = HomePage(driver)
        self.homepage.search_for_stock("NVDA")
        self.stock_page = StockPage(driver)
        header = self.stock_page.get_header()
        print(header)

        #assert
        self.assertIn("NVDA", header, "Not The Correct Page")


    def test_get_historical_data_for_stock(self,driver):

        self.stock_page = StockPage(driver)
        self.stock_page.go_to_historical_data()
        self.stock_page.download_stock_historical_data()
        does_exist = self.utils.check_file_exists(stocks)


        #assert
        self.assertTrue(does_exist, "File Doesn't Exist")



    def test_add_stock_to_watchlist(self):
        driver = self.browser.get_driver()

        self.homepage = HomePage(driver)
        self.homepage.sign_in_button_click()
        self.signin_page = SignInPage(driver)
        self.signin_page.signin_flow()

        driver.get('https://finance.yahoo.com/quote/AAPL')
        self.stock_page = StockPage(driver)
        self.stock_page.add_stock_to_watchlist()
        added_message = self.stock_page.check_added_message()

        #assert
        self.assertTrue(added_message, "Stock was not added")




    def test_get_most_active_stocks(self):
        driver = self.browser.get_driver()

        self.homepage = HomePage(driver)
        self.homepage.hover_markets_tab()
        self.homepage.go_to_most_active_stocks()
        self.most_active_stock_page = MostActiveStocksPage(driver)
        header = self.most_active_stock_page.get_header()

        #assert
        self.assertEqual(header, "Most Actives", "Wrong Page")

    def test_go_to_crypto(self):
        driver = self.browser.get_driver()
        driver.maximize_window()

        self.homepage = HomePage(driver)
        self.homepage.go_to_crypto()
        self.crypto_page = CryptoPage(driver)
        header = self.crypto_page.get_header()

        #assert
        self.assertEqual(header, "Cryptocurrencies", "Wrong Page")


    def test_stock_profile(self):
        driver = self.browser.get_driver('https://finance.yahoo.com/quote/NVDA')

        self.stock_page = StockPage(driver)
        self.stock_page.go_to_profile()
        desc = self.stock_page.get_stock_desc()
        print(desc)

        #assert
        self.assertIsNotNone(desc, "The Profile is Empty")



