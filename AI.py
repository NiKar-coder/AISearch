from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
import time


class AI:
    def __init__(self):
        firefox_options = Options()

        firefox_options.add_argument("--headless")

        self.driver = Firefox(service=Service(
            executable_path=f"{os.path.dirname(os.path.abspath(__file__))}/driver/geckodriver"), options=firefox_options)

    def ask(self, text):
        self.driver.get("https://chatgptchatapp.com/")
        time.sleep(3)
        prompt = self.driver.find_element(By.ID, "chat-input")
        prompt.send_keys(text)
        BTN_SEND_MESSAGE = self.driver.find_element(
            By.CLASS_NAME, "btn-send-message-svg")
        self.driver.execute_script(
            "arguments[0].style.display = 'inline';", BTN_SEND_MESSAGE)
        BTN_SEND_MESSAGE.click()

        time.sleep(20)

        ans = self.driver.find_element(By.CLASS_NAME, 'message-completed').text
        return ans
