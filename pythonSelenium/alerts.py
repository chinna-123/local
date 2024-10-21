import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Karikala"
d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
d.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = d.switch_to.alert
alertText = alert.text
print(alertText)

assert name in alertText
alert.accept()
# alert.dismiss()