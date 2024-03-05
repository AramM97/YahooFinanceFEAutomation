import os

from dotenv import dotenv_values


class LoginCreds:

    def __init__(self, file_path="../infra/.env"):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".env"))
        self.secrets = dotenv_values(file_path)
        #self.secrets = dotenv_values("../infra/.env")

    def get_username(self):
        return self.secrets["USERNAME"]

    def get_password(self):
        return self.secrets["PASSWORD"]


if __name__ == "__main__":
    login_creds = LoginCreds()
    username = login_creds.get_username()
    print(username)
