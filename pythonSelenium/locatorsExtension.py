import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.get("https://rahulshettyacademy.com/client")
d.find_element(By.LINK_TEXT, "Forgot password?").click()
d.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
d.find_element(By.XPATH, "//form/div[2]/input").send_keys("Hello@1234")
d.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
d.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)