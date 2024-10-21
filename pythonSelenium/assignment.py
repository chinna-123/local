import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/angularpractice/shop")
d.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

products = d.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

d.find_element(By.CSS_SELECTOR, "a[class*='btn']").click()
d.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
d.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(d, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
d.find_element(By.LINK_TEXT, "India").click()
d.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
d.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successText = d.find_element(By.CSS_SELECTOR, ".alert").text

assert "Success! Thank you!" in successText
time.sleep(3)