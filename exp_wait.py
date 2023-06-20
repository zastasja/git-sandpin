import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


try:
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    # options.add_argument("--headless=new")
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    browser.get(link)

    step = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()
# не забываем оставить пустую строку в конце файла
