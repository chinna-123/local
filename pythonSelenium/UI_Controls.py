import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = d.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


radioButtons = d.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[1].click()
assert radioButtons[1].is_selected()

assert d.find_element(By.ID, "displayed-text").is_displayed()
d.find_element(By.ID, "hide-textbox").click()
assert not d.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(2)