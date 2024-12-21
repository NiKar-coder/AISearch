from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time


firefox_options = Options()

firefox_options.add_argument("--headless")


driver = Firefox(options=firefox_options)
driver.get("https://chatgptchatapp.com/")
time.sleep(1)
prompt = driver.find_element(By.ID, "chat-input")
prompt.send_keys("dog")
BTN_SEND_MESSAGE = driver.find_element(By.CLASS_NAME, "btn-send-message-svg")
driver.execute_script(
    "arguments[0].style.display = 'inline';", BTN_SEND_MESSAGE)
BTN_SEND_MESSAGE.click()
time.sleep(3)

ans = driver.find_element(By.CLASS_NAME, 'message-completed').text
print(ans)


driver.close()
