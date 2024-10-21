import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.implicitly_wait(5)

d.get("https://the-internet.herokuapp.com/iframe")
d.switch_to.frame("mce_0_ifr")
d.find_element(By.ID, "tinymce").clear()
d.find_element(By.ID, "tinymce").send_keys("Hello")
# d.switch_to.alert.dismiss()
time.sleep(3)