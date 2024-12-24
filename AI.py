from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import asyncio


class AI:
    def __init__(self):
        firefox_options = Options()

        firefox_options.add_argument("--headless")

        self.driver = Firefox(options=firefox_options)

    async def ask(self, text):
        self.driver.get("https://chatgptchatapp.com/")
        await asyncio.sleep(3)
        prompt = self.driver.find_element(By.ID, "chat-input")
        prompt.send_keys(text)
        BTN_SEND_MESSAGE = self.driver.find_element(
            By.CLASS_NAME, "btn-send-message-svg")
        self.driver.execute_script(
            "arguments[0].style.display = 'inline';", BTN_SEND_MESSAGE)
        BTN_SEND_MESSAGE.click()

        await asyncio.sleep(20)

        self.ans = self.driver.find_element(By.CLASS_NAME, 'message-completed').text
        self.driver.close()
