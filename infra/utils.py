import os
import requests
import json
import random
import string

from selenium import webdriver

class Utils:
    def download_file(self, url, save_path):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded successfully to {save_path}")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")

    def download_file_main(self, file_url, file_name):
        # Set the path to save the file in the project directory
        file_name = file_name + ".csv"
        project_directory = os.path.dirname(os.path.realpath(__file__))
        project_directory = project_directory + '/Stock_Data/'
        save_path = os.path.join(project_directory, file_name)

        # Download the file
        self.download_file(file_url, save_path)

    def check_file_exists(self, file_name):
        # Check if the file exists in the Stock_Data directory
        stock_data_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Stock_Data')
        file_name = file_name + ".csv"
        file_path = os.path.join(stock_data_directory, file_name)
        return os.path.exists(file_path)

    def get_random_pf_name(self, length ,prefix="pf_"):
        characters = string.ascii_letters + string.digits  # You can customize this based on your requirements
        random_suffix = ''.join(random.choice(characters) for _ in range(length - len(prefix)))
        return prefix + random_suffix

    def choose_random_stocks(self, json_file_path, category="stocks", num_stocks=5):
        json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../infra/" + json_file_path ))
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        if category in data:
            all_stocks = data[category]
            selected_stocks = random.sample(all_stocks, min(num_stocks, len(all_stocks)))
            return selected_stocks
        else:
            return None


if __name__ == "__main__":
    utils = Utils()
    url = "https://query1.finance.yahoo.com/v7/finance/download/NVDA?period1=1677378518&period2=1708914518&interval=1d&events=history&includeAdjustedClose=true"
    file_name = "NVDA"

    # Download the file
    utils.download_file_main(url, file_name)

    pf_name = utils.get_random_pf_name(6)
    print(pf_name)

    json_file_path = "portfolio.json"
    selected_stocks = utils.choose_random_stocks(json_file_path)
    print(f"Selected stocks: {selected_stocks}")

    # Check if the file exists
    if utils.check_file_exists(file_name):
        print(f"{file_name}.csv exists in the Stock_Data directory.")
    else:
        print(f"{file_name}.csv does not exist in the Stock_Data directory.")
