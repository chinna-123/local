import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.get('https://rahulshettyacademy.com/angularpractice/')
d.find_element(By.NAME, 'email').send_keys('hello@gmail.com')
d.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
d.find_element(By.ID, 'exampleCheck1').click()

# XPath //tagName[@attribute='value'] //input[@type='submit']
# CSS tagName[attribute='value'] input[type='submit']

d.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Kala Bhairava")
d.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# static drop downs

dropdown = Select(d.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_index(0)
time.sleep(2)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value()

d.find_element(By.XPATH, "//input[@type='submit']").click()
message = d.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

d.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello")
d.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(2)