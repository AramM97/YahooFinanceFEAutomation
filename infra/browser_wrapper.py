import json
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BrowserWrapper:
    def __init__(self):
        self.driver = None
        print('test has started')

    def get_json_file(self):
        # Get the absolute path of the config.json file
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.json"))

        try:
            with open(file_path, "r") as f:
                config = json.load(f)
            return config
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {file_path}")
            return None


    def get_hub_url(self):
        self.json = self.get_json_file()
        return self.json["hub"]

    def get_search_query_url(self):
        self.json = self.get_json_file()
        return self.json["search_query"]


    def get_driver(self, cap, website_url="https://finance.yahoo.com"):
        self.url_hub = self.get_hub_url()
        self.driver = webdriver.Remote(command_executor=self.url_hub, options=cap)
        self.driver.get(website_url)
        return self.driver

    def get_cap_list(self):
        self.json_config = self.get_json_file()

        if "capabilities" not in self.json_config:
            raise ValueError("Missing 'capabilities' configuration in config.json")

        for browser in self.json_config["capabilities"]:
            if browser["browserName"] == "chrome":
                self.options_chrome = webdriver.ChromeOptions()
                self.options_chrome.add_argument('--platform=Windows 11')

            elif browser["browserName"] == "firefox":
                self.options_firefox = webdriver.FirefoxOptions()
                self.options_firefox.add_argument('--platform=Windows 11')

            else:
                raise ValueError(f"Unsupported browser: {browser['browserName']}")

        cap_list = [self.options_chrome, self.options_firefox]
        print(cap_list)
        return cap_list

    def get_teardown(self):
        self.driver.quit()
