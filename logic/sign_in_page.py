import time

from selenium.webdriver.common.by import By

from YahooFinanceFEAutomation.infra.login_creds import LoginCreds


class SignInPage:
    INPUT_USERNAME = "//input[@class='phone-no ']"
    INPUT_PASSWORD = "//input[@class='password']"

    SIGNIN_USER_BUTTON = "//input[@id='login-signin']"
    SIGNIN_PASSWORD_BUTTON = "//button[@class='pure-button puree-button-primary puree-spinner-button challenge-button']"



    def __init__(self, driver):
        self.driver = driver
        self.username_input = self.driver.find_element(By.XPATH, self.INPUT_USERNAME)
        self.signin_button = self.driver.find_element(By.XPATH, self.SIGNIN_USER_BUTTON)

        self.login_creds = LoginCreds("../infra/.env")


    def enter_username(self):
        self.username = self.login_creds.get_username()
        self.username_input.send_keys(self.username)

    def sumbit_username(self):
        self.signin_button.click()

    def enter_password(self):
        self.password_input = self.driver.find_element(By.XPATH, self.INPUT_PASSWORD)
        self.password = self.login_creds.get_password()
        self.password_input.send_keys(self.password)

    def submit_password(self):
        self.password_button = self.driver.find_element(By.XPATH, self.SIGNIN_PASSWORD_BUTTON)
        self.password_button.click()

    def signin_flow(self):
        self.enter_username()
        self.sumbit_username()
        time.sleep(1)
        self.enter_password()
        self.submit_password()



