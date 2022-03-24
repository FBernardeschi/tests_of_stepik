from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyperclip
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

try:
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_id("book").click()
    text1 = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text1)
    browser.find_element_by_id("answer").send_keys(calc(int(text1.text)))
    browser.find_element_by_id("solve").click()

    time.sleep(15)
finally:
    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split(": ")[-1])
    alert.accept()
    browser.quit()